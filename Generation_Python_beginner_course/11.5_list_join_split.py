s = 'BEEGEEK'
chars = list(s)
print(chars)
s = '**'.join(chars)
print(s)

# Windows OS
# В операционной системе Windows полное имя файла состоит из буквы диска, после которого ставится двоеточие и символ  "\",  затем через
# такой же символ перечисляются подкаталоги(папки), в которых находится файл, в конце пишется имя файла(C:\Windows\System32\calc.exe).
# На вход программе подается одна строка с корректным именем файла в операционной системе Windows. Напишите программу, которая разбирает
# строку на части, разделенные символом "\". Каждую часть вывести в отдельной строке.
# Формат входных данных
# На вход программе подается одна строка.
name = input().split('\\')
print(name)
print(*name, sep='\n')
