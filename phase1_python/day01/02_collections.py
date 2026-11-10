# # 保存模型每轮训练的损失
# losses = [0.95, 0.72, 0.58, 0.43, 0.35]
#
# print("第一轮 Loss:", losses[0])
# print("最后一轮 Loss:", losses[-1])
# print("前三轮 Loss:", losses[:3])
#
# # 添加新一轮的 Loss
# losses.append(0.29)
#
# # 计算平均 Loss
# avg_loss = sum(losses) / len(losses)
# print("平均 Loss:", avg_loss)
#
# # 遍历列表
# for epoch, loss in enumerate(losses, start=1):
#     print(f"Epoch {epoch}: Loss = {loss}")
#
#
# a = losses[1:4]
# print(a)


# 字典
# 模型训练配置
config = {
    "model_name": "Qwen2.5",
    "batch_size": 16,
    "learning_rate": 0.0001,
    "epochs": 10,
    "use_gpu": True
}

print("模型名称:", config["model_name"])
print("学习率:", config["learning_rate"])

# 修改训练参数
config["batch_size"] = 32

# 添加新参数
config["optimizer"] = "AdamW"

for key, value in config.items():
    print(f"{key}: {value}")

print('...................')
for key, value in config.items():
    print(key, value)