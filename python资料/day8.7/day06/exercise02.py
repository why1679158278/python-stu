# 练习：将下列英文语句按照单词进行翻转.
# To have a government that is of
# people by people for people

# people for people by people of is that government a have To

message = "To have a government that is of people by people for people"
list_result = message.split(" ")
result = " ".join(list_result[::-1])
print(result)