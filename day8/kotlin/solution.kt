import java.io.File

fun main(args: Array<String>) {
    val filename = if (args.isNotEmpty()) args[0] else "input.txt"
    val content = File(filename).readText().trim()

    println("Part 1: ${solvePart1(content)}")
    println("Part 2: ${solvePart2(content)}")
}

fun solvePart1(content: String): Int {
    val lines = content.lines()
    // TODO: Implement Part 1
    return 0
}

fun solvePart2(content: String): Long {
    val lines = content.lines()
    // TODO: Implement Part 2
    return 0
}
