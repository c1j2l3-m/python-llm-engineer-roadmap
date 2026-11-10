# 输出第一轮和最后一轮 Loss。
#
#
#
# 计算平均 Loss。
#
#
#
# 找出最小 Loss。
#
#
#
# 计算第一轮到最后一轮 Loss 的下降百分比。
#
#
#
# 使用 for 循环打印每轮 Loss。


# losses = [1.25, 0.98, 0.76, 0.61, 0.48]
#
#
# # 输出第一轮和最后一轮 Loss。
# print('第一轮：', losses[0])
# print('最后一轮：' , losses[-1])

# 计算平均 Loss。
# total = 0
# for loss in losses:
#     total += loss
# print(total)
# print(f'平均loss={total/len(losses)}')



# 找出最小 Loss。
# min = losses[0]
# for loss in losses:
#     if loss < min:
#         min = loss
# print(f"最小值为：{min}")



# # 计算第一轮到最后一轮 Loss 的下降百分比。
# losses = [1.25, 0.98, 0.76, 0.61, 0.48]
#
# first_loss = losses[0]
# last_loss = losses[-1]
#
# decrease_percent = (first_loss - last_loss) / first_loss * 100
#
# print(f"Loss 下降百分比: {decrease_percent:.2f}%")



# text = "  Hello, PYTHON World!        "
#
# print(text.strip())
# print(text.replace("Hello, PYTHON World!", "3333"))
# print('111',"".join(text))
# print(text.split(','))

sentences = [
    "I love Python",
    "I love machine learning",
    "Python is useful for machine learning"
]
# word_count = {}
#
# for sentence in sentences:
#     words = sentence.lower().split()
#     print(words)
#
#     for word in words:
#         if word in word_count:
#             word_count[word] += 1
#         else:
#             word_count[word] = 1
#
# print(word_count)




# # 将所有文本转换为小写
# for sentence in sentences:
#     words = sentence.lower()
#     print(words)



# 使用 split() 将文本拆分为单词。
for sentence in sentences:
    words = sentence.split()
    print(words)