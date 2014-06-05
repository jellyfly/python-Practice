formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one","two", "three", "four")
print formatter % (True, False, True, False)
print formatter % (formatter, formatter, formatter, formatter)
# the last line of output uses both single and double quotes for individual pieces
# the double quotes related to the single quotes inside it
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
