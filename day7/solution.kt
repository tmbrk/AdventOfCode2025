import java.io.File

fun main(args: Array<String>) {
    val filename = if (args.isNotEmpty()) args[0] else "input.txt"
    val content = File(filename).readText().trim()

    println("Part 1: ${solvePart1(content)}")
    println("Part 2: ${solvePart2(content)}")
}

fun solvePart1(content: String): Int {
    val lines = content.lines()
    val out = mutableListOf<String>()
    for (line in lines) {
        when {
            "S" in line -> {
                out.add(line.replace("S", "|"))
            }

            "^" in line -> {
                var sb = StringBuilder(line)
                for ((i, char) in out.last().withIndex()) {
                    when {
                        char == '|' && line[i] == '.' -> {
                            sb.setCharAt(i, '|')
                        }

                        char == '|' && line[i] == '^' -> {
                            sb.setCharAt(i - 1, '|')
                            sb.setCharAt(i, '*')
                            sb.setCharAt(i + 1, '|')
                        }
                    }
                }
                out.add(sb.toString())
            }

            else -> {
                out.add(out.last().replace("*", ".").replace("^", "."))
            }
        }
    }

    val result =
        out.fold(0) { acc, str ->
            acc + str.count { it == '*' }
        }
    return result
}

val cache = mutableMapOf<Pair<Int, List<String>>, Long>()

fun calcPath(
    line: Int,
    tree: List<String>,
): Long {
    when {
        cache.get(Pair(line, tree)) != null -> {
            return cache[Pair(line, tree)]!!
        }

        tree.isEmpty() -> {
            return 1
        }

        else -> {
            var out: Long = 0
            for ((i, char) in tree.first().withIndex()) {
                when {
                    char == '^' && i == line -> {
                        out += calcPath(i - 1, tree.drop(1))
                        out += calcPath(i + 1, tree.drop(1))
                    }

                    char == '.' && i == line -> {
                        out += calcPath(line, tree.drop(1))
                    }
                }
            }
            return cache.getOrPut(Pair(line, tree)) { out }
        }
    }
}

fun solvePart2(content: String): Long {
    val lines = content.lines()
    return calcPath(lines.first().indexOf('S'), lines.drop(1))
}
