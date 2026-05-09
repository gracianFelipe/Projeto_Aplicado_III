import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(
    page_title="Recomendador de Restaurantes",
    page_icon="🍽️",
    layout="wide"
)

@st.cache_data
def carregar_dados(caminho_csv: str) -> pd.DataFrame:
    df = pd.read_csv(caminho_csv)
    df = df.dropna(subset=["name", "texto_recomendacao_limpo"]).copy()
    df["name"] = df["name"].astype(str).str.strip()
    df["texto_recomendacao_limpo"] = df["texto_recomendacao_limpo"].astype(str).str.strip()
    df = df[df["name"] != ""]
    df = df[df["texto_recomendacao_limpo"] != ""]
    df = df.drop_duplicates().reset_index(drop=True)
    return df

@st.cache_resource
def preparar_modelo(df: pd.DataFrame):
    vetorizador = TfidfVectorizer(
        stop_words="english",
        ngram_range=(1, 2),
        min_df=2
    )
    matriz_tfidf = vetorizador.fit_transform(df["texto_recomendacao_limpo"])

    # Índice por nome; remove duplicados pelo primeiro nome encontrado
    indices = pd.Series(df.index, index=df["name"]).drop_duplicates()

    return vetorizador, matriz_tfidf, indices

def recomendar_restaurantes(
    nome_restaurante: str,
    df: pd.DataFrame,
    matriz_tfidf,
    indices,
    top_n: int = 5
) -> pd.DataFrame:
    if nome_restaurante not in indices:
        return pd.DataFrame()

    idx = indices[nome_restaurante]

    # Calcula similaridade apenas do restaurante escolhido contra toda a base
    similaridades = cosine_similarity(matriz_tfidf[idx], matriz_tfidf).flatten()

    # Ordena os índices do mais similar para o menos similar
    indices_ordenados = similaridades.argsort()[::-1]

    # Remove o próprio restaurante
    indices_ordenados = [i for i in indices_ordenados if i != idx][:top_n]

    resultado = df.iloc[indices_ordenados].copy()
    resultado["similaridade"] = similaridades[indices_ordenados]

    colunas_saida = ["name", "category", "price_range", "estado", "similaridade"]
    colunas_saida = [c for c in colunas_saida if c in resultado.columns]

    return resultado[colunas_saida].reset_index(drop=True)

# ======================
# Interface
# ======================

st.title("🍽️ Sistema de Recomendação de Restaurantes")
st.markdown(
    """
    Esta aplicação demonstra uma prova de conceito de recomendação baseada em conteúdo,
    desenvolvida no Projeto Aplicado III a partir da base **iFood Restaurants Data**.
    """
)

df = carregar_dados("restaurantes_app_10porcento.csv")
_, matriz_tfidf, indices = preparar_modelo(df)

st.subheader("Selecione um restaurante de referência")

nomes_restaurantes = sorted(df["name"].dropna().unique().tolist())

restaurante_escolhido = st.selectbox(
    "Restaurante",
    options=nomes_restaurantes,
    index=0
)

top_n = st.slider(
    "Quantidade de recomendações",
    min_value=3,
    max_value=10,
    value=5,
    step=1
)

if st.button("Gerar recomendações"):
    recomendacoes = recomendar_restaurantes(
        nome_restaurante=restaurante_escolhido,
        df=df,
        matriz_tfidf=matriz_tfidf,
        indices=indices,
        top_n=top_n
    )

    st.markdown(f"### Recomendações para: **{restaurante_escolhido}**")

    if recomendacoes.empty:
        st.warning("Não foi possível gerar recomendações para o restaurante selecionado.")
    else:
        recomendacoes["similaridade"] = recomendacoes["similaridade"].round(4)
        recomendacoes = recomendacoes.rename(
            columns={
                "name": "Restaurante",
                "category": "Categoria",
                "price_range": "Faixa de preço",
                "estado": "Estado",
                "similaridade": "Similaridade"
            }
        )

        st.markdown("### Top recomendações encontradas")
        st.markdown(
            f"**Restaurante selecionado:** {restaurante_escolhido}  \n"
            f"**Quantidade de recomendações:** {top_n}"
        )

        colunas = st.columns(3)

        for i, (_, row) in enumerate(recomendacoes.iterrows()):
            with colunas[i % 3]:
                with st.container(border=True):
                    st.markdown(f"**{row['Restaurante']}**")
                    st.markdown(
                        f"""
                        <div style="
                            display: inline-block;
                            padding: 4px 8px;
                            border-radius: 999px;
                            background-color: #ecfdf5;
                            color: #065f46;
                            font-size: 11px;
                            font-weight: 700;
                            margin-top: 2px;
                            margin-bottom: 6px;
                        ">
                            Similaridade: {row['Similaridade']}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                    st.markdown(f"<span style='font-size:12px;'>Categoria: {row['Categoria']}</span>", unsafe_allow_html=True)
                    st.markdown(f"<span style='font-size:12px;'>Faixa de preço: {row['Faixa de preço']}</span>", unsafe_allow_html=True)
                    st.markdown(f"<span style='font-size:12px;'>Estado: {row['Estado']}</span>", unsafe_allow_html=True)

st.markdown("---")
st.caption("Projeto Aplicado III — Prova de conceito de recomendação de restaurantes")