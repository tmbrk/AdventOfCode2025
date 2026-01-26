import java.io.File

fun main() {
    val content = File("input_test.txt").readText().trim()
    val result = solvePart1(content)
    println("Testing Part 1: Expected 40, Got $result")
    assert(result == 40) { "Test failed: Expected 40, Got $result" }
    println("Test passed!")
}
