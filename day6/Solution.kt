import java.io.File

fun main(args: Array<String>) {
    val filename = if (args.isNotEmpty()) args[0] else "input.txt"
    val content = File(filename).readText()
    
    solvePart1(content)
    solvePart2(content)
}

fun solvePart1(content: String) {
    val lines = content.lines().filter { it.isNotEmpty() }
    if (lines.isEmpty()) return

    // Parse all lines as rows of tokens
    val data = lines.map { line -> 
        line.trim().split("\\s+".toRegex()) 
    }

    if (data.isEmpty()) return

    // Last row contains operators
    val operators = data.last()
    
    // Operands are all rows except the last
    val operandRows = data.dropLast(1)
    
    val results = mutableListOf<Long>()
    
    // Iterate columns. Assuming consistent width based on operator count or just iterating available.
    // The Python code zips columns.
    
    val numCols = operators.size
    
    for (colIdx in 0 until numCols) {
        val operands = mutableListOf<Long>()
        for (row in operandRows) {
            if (colIdx < row.size) {
                row[colIdx].toLongOrNull()?.let { operands.add(it) }
            }
        }
        
        if (operands.isNotEmpty()) {
            val op = operators[colIdx]
            results.add(calculate(operands, op))
        }
    }
    
    println("Part 1: ${results.sum()}")
}

fun solvePart2(content: String) {
    val lines = content.lines().filter { it.isNotEmpty() } // Note: keep lines but filter empty ones at end if any?
    // Actually, split('\n') might give an empty string at the end. 
    // Python's file iteration yields lines.
    
    if (lines.isEmpty()) return
    
    val maxLen = lines.maxOfOrNull { it.length } ?: 0
    
    // Pad lines
    val grid = lines.map { line ->
        line.padEnd(maxLen, ' ').toCharArray()
    }
    
    val lastRowIdx = grid.size - 1
    val operatorRow = grid[lastRowIdx]
    val numberGrid = grid.dropLast(1)
    
    val columnStrings = mutableListOf<String>()
    
    for (col in 0 until maxLen) {
        val sb = StringBuilder()
        for (row in numberGrid) {
            sb.append(row[col])
        }
        columnStrings.add(sb.toString().trim())
    }
    
    val operandGroups = mutableListOf<List<Long>>()
    var currentGroup = mutableListOf<Long>()
    
    for (s in columnStrings) {
        if (s.isEmpty()) {
            if (currentGroup.isNotEmpty()) {
                operandGroups.add(currentGroup)
                currentGroup = mutableListOf()
            }
        } else {
            s.toLongOrNull()?.let { currentGroup.add(it) }
        }
    }
    if (currentGroup.isNotEmpty()) {
        operandGroups.add(currentGroup)
    }
    
    val validOperators = operatorRow.filter { !it.isWhitespace() }.map { it.toString() }
    
    val results = mutableListOf<Long>()
    
    // Zip groups and operators
    val count = minOf(operandGroups.size, validOperators.size)
    for (i in 0 until count) {
        results.add(calculate(operandGroups[i], validOperators[i]))
    }
    
    println("Part 2: ${results.sum()}")
}

fun calculate(operands: List<Long>, op: String): Long {
    if (operands.isEmpty()) return 0
    
    // reduce
    var acc = operands[0]
    for (i in 1 until operands.size) {
        val `val` = operands[i]
        when (op) {
            "*" -> acc *= `val`
            "+" -> acc += `val`
            "-" -> acc -= `val`
            "/" -> acc /= `val` // Integer division
            else -> throw IllegalArgumentException("Unknown operator: $op")
        }
    }
    return acc
}
