import Analizador as Analizer

# Practice TEXT ANALYSIS
text = "Lorem ipsum dolor! diam amet, consetetur Lorem magna."  \
"sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."

word = "et"
analized = Analizer.TextAnalyzer(text)
frecuency = analized.freqOf(word)
print(f"The word {word} appears {frecuency} times")
