import streamlit as st
from carregar_graficos import carregar_graficos_plotly

def main():
    # Carregar os gráficos
    st.sidebar.title("Configurações")
    st.sidebar.info("Carregando os gráficos...")
    graficos = carregar_graficos_plotly()

    # Título do Dashboard
    st.title("Dashboard de Análises Políticas e Econômicas")
    st.markdown(
        """
        Este dashboard apresenta uma análise detalhada de indicadores políticos, econômicos, sociais, e culturais organizados por categorias.
        Selecione uma aba para explorar os gráficos.
        """
    )

    # Criar as abas principais
    aba = st.sidebar.selectbox(
        "Selecione a Dimensão",
        [
            "Resumo dos Regimes e Composição Política",
            "Indicadores Econômicos",
            "Indicadores de Desenvolvimento Humano",
            "Indicadores Sociais",
            "Indicadores Ambientais e de Sustentabilidade",
            "Indicadores Institucionais e de Governança",
            "Indicadores Demográficos",
            "Indicadores Culturais"
        ]
    )

    # Mostrar gráficos com base na aba selecionada
    if aba == "Resumo dos Regimes e Composição Política":
        st.subheader("Resumo dos Regimes e Composição Política")
        st.plotly_chart(graficos["fig_pslri_regime"], use_container_width=True)
        st.plotly_chart(graficos["fig_pslri_distribuicao"], use_container_width=True)

    elif aba == "Indicadores Econômicos":
        st.subheader("Indicadores Econômicos")
        st.plotly_chart(graficos["fig_pib_vida"], use_container_width=True)
        st.plotly_chart(graficos["fig_pib_regime"], use_container_width=True)
        st.plotly_chart(graficos["fig_pib_pslri"], use_container_width=True)
        st.plotly_chart(graficos["fig_crescimento_pib"], use_container_width=True)
        st.plotly_chart(graficos["fig_crescimento_pib_pslri"], use_container_width=True)
        st.plotly_chart(graficos["fig_gini_regime"], use_container_width=True)
        st.plotly_chart(graficos["fig_gini_pslri"], use_container_width=True)
        st.plotly_chart(graficos["fig_balanca_regime"], use_container_width=True)
        st.plotly_chart(graficos["fig_balanca_pslri"], use_container_width=True)

    elif aba == "Indicadores de Desenvolvimento Humano":
        st.subheader("Indicadores de Desenvolvimento Humano")
        st.plotly_chart(graficos["fig_idh_regime_politico"], use_container_width=True)
        st.plotly_chart(graficos["fig_idh_pslri"], use_container_width=True)
        st.plotly_chart(graficos["fig_expectativa_vida"], use_container_width=True)
        st.plotly_chart(graficos["fig_expectativa_vida_pslri"], use_container_width=True)
        st.plotly_chart(graficos["fig_alfabetizacao_politico"], use_container_width=True)
        st.plotly_chart(graficos["fig_alfabetizacao_pslri"], use_container_width=True)

    elif aba == "Indicadores Sociais":
        st.subheader("Indicadores Sociais")
        st.plotly_chart(graficos["fig_taxa_pobreza_regime"], use_container_width=True)
        st.plotly_chart(graficos["fig_taxa_pobreza_pslri"], use_container_width=True)
        st.plotly_chart(graficos["fig_desigualdade_genero_regime"], use_container_width=True)
        st.plotly_chart(graficos["fig_desigualdade_genero_pslri"], use_container_width=True)
        st.plotly_chart(graficos["fig_taxa_desemprego_regime"], use_container_width=True)
        st.plotly_chart(graficos["fig_taxa_desemprego_pslri"], use_container_width=True)

    elif aba == "Indicadores Ambientais e de Sustentabilidade":
        st.subheader("Indicadores Ambientais e de Sustentabilidade")
        st.plotly_chart(graficos["fig_pegada_ecologica_regime"], use_container_width=True)
        st.plotly_chart(graficos["fig_pegada_ecologica_pslri"], use_container_width=True)
        st.plotly_chart(graficos["fig_emissoes_co2_politico"], use_container_width=True)
        st.plotly_chart(graficos["fig_emissoes_co2_pslri"], use_container_width=True)

    elif aba == "Indicadores Institucionais e de Governança":
        st.subheader("Indicadores Institucionais e de Governança")
        st.plotly_chart(graficos["fig_corrupcao_regime"], use_container_width=True)
        st.plotly_chart(graficos["fig_corrupcao_pslri"], use_container_width=True)
        st.plotly_chart(graficos["fig_liberdade_economica"], use_container_width=True)
        st.plotly_chart(graficos["fig_liberdade_economica_pslri"], use_container_width=True)
        st.plotly_chart(graficos["fig_democracia_liberal"], use_container_width=True)
        st.plotly_chart(graficos["fig_democracia_liberal_pslri"], use_container_width=True)

    elif aba == "Indicadores Demográficos":
        st.subheader("Indicadores Demográficos")
        st.plotly_chart(graficos["fig_crescimento_populacional_regime"], use_container_width=True)
        st.plotly_chart(graficos["fig_crescimento_populacional_pslri"], use_container_width=True)
        st.plotly_chart(graficos["fig_populacao_urbana_regime"], use_container_width=True)
        st.plotly_chart(graficos["fig_populacao_urbana_pslri"], use_container_width=True)

    elif aba == "Indicadores Culturais":
        st.subheader("Indicadores Culturais")
        st.plotly_chart(graficos["fig_despesas_culturais_politico"], use_container_width=True)
        st.plotly_chart(graficos["fig_despesas_culturais_pslri"], use_container_width=True)
        st.plotly_chart(graficos["fig_satisfacao_vida_regime"], use_container_width=True)
        st.plotly_chart(graficos["fig_satisfacao_vida_pslri"], use_container_width=True)
        st.plotly_chart(graficos["fig_cultura_democratica_regime"], use_container_width=True)
        st.plotly_chart(graficos["fig_cultura_democratica_pslri"], use_container_width=True)

if __name__ == "__main__":
    main()
