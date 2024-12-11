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

    # Função para exibir gráficos mantendo tamanhos originais
    def exibir_grafico_fixo(fig):
        # Adicionar configurações para não redimensionar o gráfico
        st.plotly_chart(
            fig,
            use_container_width=False,
            config={
                "responsive": False,  # Impedir redimensionamento automático
                "displayModeBar": True  # Mostrar barra de ferramentas para controle
            }
        )

    # Mostrar gráficos com base na aba selecionada
    if aba == "Resumo dos Regimes e Composição Política":
        st.subheader("Resumo dos Regimes e Composição Política")
        exibir_grafico_fixo(graficos["fig_pslri_regime"])
        exibir_grafico_fixo(graficos["fig_pslri_distribuicao"])

    elif aba == "Indicadores Econômicos":
        st.subheader("Indicadores Econômicos")
        exibir_grafico_fixo(graficos["fig_pib_vida"])
        exibir_grafico_fixo(graficos["fig_pib_regime"])
        exibir_grafico_fixo(graficos["fig_pib_pslri"])
        exibir_grafico_fixo(graficos["fig_crescimento_pib"])
        exibir_grafico_fixo(graficos["fig_crescimento_pib_pslri"])
        exibir_grafico_fixo(graficos["fig_gini_regime"])
        exibir_grafico_fixo(graficos["fig_gini_pslri"])
        exibir_grafico_fixo(graficos["fig_balanca_regime"])
        exibir_grafico_fixo(graficos["fig_balanca_pslri"])

    elif aba == "Indicadores de Desenvolvimento Humano":
        st.subheader("Indicadores de Desenvolvimento Humano")
        exibir_grafico_fixo(graficos["fig_idh_regime_politico"])
        exibir_grafico_fixo(graficos["fig_idh_pslri"])
        exibir_grafico_fixo(graficos["fig_expectativa_vida"])
        exibir_grafico_fixo(graficos["fig_expectativa_vida_pslri"])
        exibir_grafico_fixo(graficos["fig_alfabetizacao_politico"])
        exibir_grafico_fixo(graficos["fig_alfabetizacao_pslri"])

    elif aba == "Indicadores Sociais":
        st.subheader("Indicadores Sociais")
        exibir_grafico_fixo(graficos["fig_taxa_pobreza_regime"])
        exibir_grafico_fixo(graficos["fig_taxa_pobreza_pslri"])
        exibir_grafico_fixo(graficos["fig_desigualdade_genero_regime"])
        exibir_grafico_fixo(graficos["fig_desigualdade_genero_pslri"])
        exibir_grafico_fixo(graficos["fig_taxa_desemprego_regime"])
        exibir_grafico_fixo(graficos["fig_taxa_desemprego_pslri"])

    elif aba == "Indicadores Ambientais e de Sustentabilidade":
        st.subheader("Indicadores Ambientais e de Sustentabilidade")
        exibir_grafico_fixo(graficos["fig_pegada_ecologica_regime"])
        exibir_grafico_fixo(graficos["fig_pegada_ecologica_pslri"])
        exibir_grafico_fixo(graficos["fig_emissoes_co2_politico"])
        exibir_grafico_fixo(graficos["fig_emissoes_co2_pslri"])

    elif aba == "Indicadores Institucionais e de Governança":
        st.subheader("Indicadores Institucionais e de Governança")
        exibir_grafico_fixo(graficos["fig_corrupcao_regime"])
        exibir_grafico_fixo(graficos["fig_corrupcao_pslri"])
        exibir_grafico_fixo(graficos["fig_liberdade_economica"])
        exibir_grafico_fixo(graficos["fig_liberdade_economica_pslri"])
        exibir_grafico_fixo(graficos["fig_democracia_liberal"])
        exibir_grafico_fixo(graficos["fig_democracia_liberal_pslri"])

    elif aba == "Indicadores Demográficos":
        st.subheader("Indicadores Demográficos")
        exibir_grafico_fixo(graficos["fig_crescimento_populacional_regime"])
        exibir_grafico_fixo(graficos["fig_crescimento_populacional_pslri"])
        exibir_grafico_fixo(graficos["fig_populacao_urbana_regime"])
        exibir_grafico_fixo(graficos["fig_populacao_urbana_pslri"])

    elif aba == "Indicadores Culturais":
        st.subheader("Indicadores Culturais")
        exibir_grafico_fixo(graficos["fig_despesas_culturais_politico"])
        exibir_grafico_fixo(graficos["fig_despesas_culturais_pslri"])
        exibir_grafico_fixo(graficos["fig_satisfacao_vida_regime"])
        exibir_grafico_fixo(graficos["fig_satisfacao_vida_pslri"])
        exibir_grafico_fixo(graficos["fig_cultura_democratica_regime"])
        exibir_grafico_fixo(graficos["fig_cultura_democratica_pslri"])

if __name__ == "__main__":
    main()
