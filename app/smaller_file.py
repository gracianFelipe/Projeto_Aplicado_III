import pandas as pd

df = pd.read_csv("restaurantes_app.csv")

df_10 = (
    df.sample(frac=0.10, random_state=42)
      .reset_index(drop=True)
)

df_10.to_csv("restaurantes_app_10porcento.csv", index=False, encoding="utf-8")

print("Arquivo gerado com sucesso:", df_10.shape)