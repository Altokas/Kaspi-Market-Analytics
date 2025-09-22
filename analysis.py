import pandas as pd

# Загружаем данные
df = pd.read_csv("data/transactions.csv")

print("📊 Первые строки данных:")
print(df.head())

print("\n🔢 Общая статистика:")
print(df.describe())

print("\n💰 Общая выручка:", (df["Quantity"] * df["Price"]).sum())

print("\n📦 Выручка по категориям:")
print(df.groupby("Category")["Price"].sum())

