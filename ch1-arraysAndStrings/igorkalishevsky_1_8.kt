package ctci.arraysandstrings

import org.junit.jupiter.api.Assertions.assertTrue
import org.junit.jupiter.api.Test

class ZeroMatrixTest {
    @Test
    fun test1() {
        val array = parseArray(
            """
            1 1 1 1 1
            0 1 1 1 1
            1 1 0 1 1
        """.trimIndent()
        )
        val expected = parseArray(
            """
            0 1 0 1 1
            0 0 0 0 0
            0 0 0 0 0
        """.trimIndent()
        )

        assertTrue(array.cross().contentDeepEquals(expected))
    }

    @Test
    fun test2() {
        val array = parseArray(
            """
            1 1 1 1 1
            1 1 0 1 1
            1 1 1 1 1
        """.trimIndent()
        )
        val expected = parseArray(
            """
            1 1 0 1 1
            0 0 0 0 0
            1 1 0 1 1
        """.trimIndent()
        )

        assertTrue(array.cross().contentDeepEquals(expected))
    }

    companion object {
        fun <T> Array<Array<T>>.findCoords(value: T): List<Pair<Int, Int>> =
            flatMapIndexed { i, row ->
                row.mapIndexedNotNull { j, col ->
                    if (col == value) {
                        i to j
                    } else {
                        null
                    }
                }
            }

        fun Array<Array<Int>>.cross(): Array<Array<Int>> {
            findCoords(0).forEach { (i, j) ->
                val row = this[i]
                for (index in row.indices) {
                    row[index] = 0
                }
                for (index in indices) {
                    this[index][j] = 0
                }
            }
            return this
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
    }
}

