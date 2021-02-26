
package ctci.arraysandstrings

import ctci.arraysandstrings.StringCompressor.Companion.compress
import ctci.arraysandstrings.StringCompressor.Companion.compressMp
import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.Test
import java.util.concurrent.ExecutorCompletionService
import java.util.concurrent.Executors
import java.util.concurrent.Future
import kotlin.system.measureTimeMillis

class StringCompressorTest {
    @Test
    fun testMp() {
        val (raw, compressed) = prepareDataset(1000000, 100)
        assertEquals(compressed, raw.compress())
        assertEquals(compressed, raw.compressMp(10))
    }

    @Test
    fun performance() {
        val (raw, _) = prepareDataset(1000000, 100)
        val singleThreadTimes = mutableListOf<Long>()
        val multiThreadTimes = mutableListOf<Long>()
        for (i in 0..20) {
            measureTimeMillis {
                raw.compress()
            }.also { singleThreadTimes.add(it) }
            measureTimeMillis {
                raw.compressMp(10)
            }.also { multiThreadTimes.add(it) }
        }
        println("Average single threaded: ${singleThreadTimes.average()}")
        println("Average multi threaded: ${multiThreadTimes.average()}")
    }

    @Test
    fun testSample() {
        val groups = listOf(
            "aaaaaaa",
            "rrrr",
            "llllll",
            "aaaaa",
            "bbb",
            "ccc",
            "lll",
            "aaaa",
            "bb",
            "s"
        )

        val rawString = groups.joinToString("")
        val compressed = rawString.compress()
        assertEquals("a7r4l6a5b3c3l3a4b2s1", compressed)

        val compressor = StringCompressor(rawString)
        val compressedMp = compressor.compress(10)
        assertEquals(compressed, compressedMp)
    }

    @Test
    fun testIneffectiveCompression() {
        val rawString = "qwerty"
        assertEquals(rawString, rawString.compress())
        assertEquals(rawString, rawString.compressMp(2))
    }

    private fun prepareDataset(numReps: Int, maxSize: Int): Pair<String, String> {
        val chars = ('a'..'z').toList()
        val compressedParts = mutableListOf<String>()
        val rawParts = mutableListOf<String>()

        (0 until numReps).forEach { i ->
            val chunkSize = i % maxSize + 1
            val char = chars[i % chars.size]
            rawParts.add(char.toString().repeat(chunkSize))
            compressedParts.add("$char$chunkSize")
        }

        val rawString = rawParts.joinToString("")
        val compressed = compressedParts.joinToString("")

        return rawString to compressed
    }
}

class StringCompressor(private val rawString: String) {
    fun compress(numThreads: Int, printChunks: Boolean = false): String {
        var chunk: Chunk? = rawString.chunkByLength(numThreads)
        chunk = rawString.refineMargins(chunk!!)

        if (printChunks) {
            chunk.printAll()
        }

        val completionService = ExecutorCompletionService<String>(Executors.newFixedThreadPool(chunk.totalSize))
        val futures = mutableListOf<Future<String>>()
        while (chunk != null) {
            val currentChunk = chunk
            completionService
                .submit { rawString.compress(currentChunk) }
                .apply { futures.add(this) }

            chunk = chunk.next
        }

        return futures.joinToString("") { it.get() }
    }

    private fun String.refineMargins(first: Chunk): Chunk {
        var current = first
        var next = current.next
        var oldValid = current

        while (next != null) {
            if (this[current.right] == this[next.left]) {
                current.right--
                next.left--
            } else {
                current = current.next ?: break
                next = current.next
            }
            if (!current.isValid) {
                val newCurrent = current.remove()
                oldValid = newCurrent ?: current.first
                current = newCurrent ?: break
                next = current.next
            }
        }
        return oldValid.first
    }

    private fun String.chunkByLength(num: Int = 4): Chunk {
        if (num <= 0 || num > length) {
            throw IllegalArgumentException("$num shall not pass")
        }

        val partSize = length.toDouble() / num
        var oldNext: Chunk? = null

        ((num - 1) downTo 0).forEach { index ->
            val left = index * partSize
            val right = partSize * (index + 1)
            val next = Chunk(left = left.toInt(), right = right.toInt() - 1, prev = null, next = oldNext)
            oldNext?.prev = next
            oldNext = next
        }

        return oldNext!!
    }

    companion object {
        fun String.compress(): String {
            val compressed = compress(0, length - 1)
            if (compressed.length > length) {
                return this
            }
            return compressed
        }

        fun String.compressMp(numThreads: Int): String {
            val compressed = StringCompressor(this).compress(numThreads)
            if (compressed.length > length) {
                return this
            }
            return compressed
        }

        private fun String.compress(chunk: Chunk): String {
            return compress(chunk.left, chunk.right)
        }

        private fun String.compress(left: Int, rightInclusive: Int): String {
            val feeder = Feeder()
            (left..rightInclusive).forEach { i ->
                feeder.feed(this[i])
            }
            return feeder.toString()
        }
    }
}

private class Feeder {
    private val repetitions = mutableListOf<Repetition>()
    fun feed(ch: Char) {
        if (repetitions.isEmpty()) {
            repetitions.add(Repetition(ch, 0))
        }
        val last = repetitions.last()
        if (last.ch == ch) {
            last.num++
        } else {
            repetitions.add(Repetition(ch, 1))
        }
    }

    override fun toString(): String {
        return repetitions.joinToString("")
    }

    private data class Repetition(val ch: Char, var num: Int) {
        override fun toString(): String {
            return "$ch$num"
        }
    }
}

private class Chunk(var left: Int, var right: Int, var prev: Chunk?, var next: Chunk?) {
    override fun toString(): String {
        return "Span(${repr(this)}; prev=${repr(prev)}, next=${repr(next)})"
    }

    private fun repr(chunk: Chunk?) = chunk?.let {
        "(${it.left}; ${it.right})"
    }

    val totalSize: Int
        get() {
            var counter = 0
            var chunk: Chunk? = first
            while (chunk != null) {
                counter++
                chunk = chunk.next
            }
            return counter
        }


    val isValid: Boolean get() = right + 1 > left

    val first: Chunk
        get() {
            var span = this
            while (span.prev != null) {
                span.prev?.let {
                    span = it
                }
            }
            return span
        }

    fun remove(): Chunk? {
        val oldNext = next
        prev?.next = next
        next?.prev = prev

        next = null
        prev = null
        return oldNext
    }

    fun printAll() {
        var chunk: Chunk? = first
        while (chunk != null) {
            println(chunk)
            chunk = chunk.next
        }
    }
}
