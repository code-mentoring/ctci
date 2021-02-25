package ctci.arraysandstrings

import org.junit.jupiter.api.Assertions.assertTrue
import org.junit.jupiter.api.Disabled
import org.junit.jupiter.api.Test

class MatrixRotatorTest {
    private val x4 = parseArray(
        """
         1  2  3  4
         5  6  7  8
         9 10 11 12
        13 14 15 16
        """.trimIndent()
    )

    private val x4Rotated = parseArray(
        """
         13  9  5  1
         14 10  6  2
         15 11  7  3
         16 12  8  4
        """.trimIndent()
    )

    private val x5 = parseArray(
        """
         1  2  3  4  5
         6  7  8  9 10
        11 12 13 14 15
        16 17 18 19 20
        21 22 23 24 25
        """.trimIndent()
    )

    private val x5Rotated = parseArray(
        """
         21 16 11  6  1
         22 17 12  7  2
         23 18 13  8  3
         24 19 14  9  4
         25 20 15 10  5
        """.trimIndent()
    )

    @Test
    fun rotate() {
        val array = x4.deepClone()
        val rotated = array.rotate()
        assertTrue(rotated.contentDeepEquals(x4Rotated))
        array.rotateInPlace()

        assertTrue(array.contentDeepEquals(x4Rotated))
    }

    @Test
    fun youSpinMeRound() {
        val array = x4.deepClone()
        array.rotateInPlace(verbose = false)
        assertTrue(array.contentDeepEquals(x4Rotated))
    }

    @Test
    fun oddRowColNumber() {
        val array = x5.deepClone()
        array.rotateInPlace(verbose = false)
        assertTrue(array.contentDeepEquals(x5Rotated))
    }

    @Test
    @Disabled
    fun sample() {
        val array = Array(4) {
            Array(4) { 0 }
        }
        array.reset()
        array.prepare()
        array.print()

        array.rotate().print()
        array.rotateInPlace(verbose = true).print()
    }

    companion object {
        fun Array<Array<Int>>.rotateInPlace(verbose: Boolean = false): Array<Array<Int>> {
            //  1  2  3  4
            //  5  6  7  8
            //  9 10 11 12
            // 13 14 15 16
            // Start with corners
            // Store 4  | Store 8
            //  1 -> 4  |  2 -> 8
            // 13 -> 1  |  9 -> 2
            // 16 -> 13 | 15 -> 9
            //  4 -> 16 |  8 -> 15

            val debug = mutableListOf<String>()
            for (i in (0 until size / 2)) {
                for (j in (i until size - i - 1)) {
                    val tmp = this[j][size - i - 1]

                    val ops = listOf(
                        "[$i; $j] Store ${this[j][size - i - 1]}",
                        "[$i; $j] ${this[i][j]} -> ${this[j][size - i - 1]}",
                        "[$i; $j] ${this[size - j - 1][i]} -> ${this[i][j]}",
                        "[$i; $j] ${this[size - i - 1][size - j - 1]} -> ${this[size - j - 1][i]}",
                        "[$i; $j] Restore $tmp -> ${this[size - i - 1][size - j - 1]}",
                        "==="
                    )
                    debug.add(ops.joinToString("\n"))

                    this[j][size - i - 1] = this[i][j]
                    this[i][j] = this[size - j - 1][i]
                    this[size - j - 1][i] = this[size - i - 1][size - j - 1]
                    this[size - i - 1][size - j - 1] = tmp
                }
                debug.add(repr())
            }

            if (verbose) {
                println(debug.joinToString("\n"))
            }

            return this
        }

        fun Array<Array<Int>>.rotate(): Array<Array<Int>> {
            val clone = deepClone()
            for (i in indices) {
                for (j in indices) {
                    clone[i][j] = this[size - j - 1][i]
                }
            }
            return clone
        }

        fun parseArray(stringArrayRepr: String): Array<Array<Int>> {
            return stringArrayRepr.trim().split("\n")
                .map { row ->
                    row.trim().split("\\s+".toRegex())
                        .map { col -> col.toInt() }
                        .toTypedArray()
                }
                .toTypedArray()
        }

        fun Array<Array<Int>>.prepare() {
            var counter = 1
            for (i in indices) {
                for (j in this[i].indices) {
                    this[i][j] = counter++
                }
            }
        }

        fun Array<Array<Int>>.reset() {
            for (i in indices) {
                for (j in this[i].indices) {
                    this[i][j] = 0
                }
            }
        }

        fun <T> Array<Array<T>>.max(): T where T : Comparable<T> =
            mapNotNull { it.maxOrNull() }
                .maxOrNull() ?: error("Null shall not pass")


        fun <T> Array<Array<T>>.repr(): String
                where T : Comparable<T> {
            val strings = mutableListOf<String>()
            val padding = max().toString().length + 1
            for (i in indices) {
                val rowParts = mutableListOf<String>()
                for (j in this[i].indices) {
                    rowParts.add(this[i][j].toString().padStart(padding))
                }
                strings.add(rowParts.joinToString("", postfix = "\n"))
            }
            return strings.joinToString("")
        }


        fun <T> Array<Array<T>>.print() where T : Comparable<T> {
            println(repr())
        }


        fun Array<Array<Int>>.deepClone(): Array<Array<Int>> {
            val clone = clone()
            for (i in clone.indices) {
                clone[i] = clone[i].clone()
            }
            return clone
        }

    }
}


