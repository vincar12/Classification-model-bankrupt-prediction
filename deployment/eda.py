# import library
import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

# app
def run():

    # create title
    st.title('Company Bankruptcy Analysis')
    # separator
    st.markdown('---')

    # create subheader
    st.subheader('Exploratory Data Analysis untuk analisa dataset Taiwanese Bankruptcy Prediction')
    # insert image
    image1 = Image.open('image1234.jpg')
    st.image(image1, caption='Ilustrasi dokumen bangkrut')
    # write image description
    st.write('Proyek ini berdasarkan dataset Taiwanese Bankruptcy Prediction dari UCI Machine Learning. Laman ini dibuat untuk eksplorasi untuk memahami data lebih lanjut.')
    # separator
    st.markdown('---')

    # show dataframe
    st.write('#### Dataset Taiwanese Bankruptcy Prediction')
    df = pd.read_csv('data.csv')
    st.dataframe(df)
    # separator
    st.markdown('---')
    # strip whitespace
    df.columns = df.columns.str.strip()

    # create bar chart1
    # mapping variable name
    urutan = {0: 'Tidak Bangkrut', 1: 'Bangkrut'}
    df['Bankrupt?'] = df['Bankrupt?'].map(urutan)
    # grouping by bankrupt
    bankrupt = df.groupby("Bankrupt?")["Net Income Flag"].count()
    bankrupt = bankrupt.reset_index()
    # pie chart figure
    st.write('#### Plot Jumlah Data Bangkrut dan Tidak Bangkrut')
    fig = px.pie(bankrupt, names="Bankrupt?", 
                values="Net Income Flag") 
    # display pie chart 
    st.plotly_chart(fig)
    # description
    st.write('Jumlah usaha yang bangkrut hanya sebanyak 220 atau sekitar 3%, dibandingkan dengan jumlah usaha yang tidak bangkrut sebanyak 6599 atau sekitar 97%. Dari perbandingan target yang sangat jauh jumlah datanya, dapat ditarik informasi bahwa data akan perlu dilakukan balancing agar lebih seimbang.')

    # create bar chart2
    # grouping by bankrupt and averaging margins
    topmargin = df.groupby("Bankrupt?")[['Operating Gross Margin','Realized Sales Gross Margin']].mean().sort_values(ascending=False, by='Operating Gross Margin')
    topmargin = topmargin.reset_index()
    # bar chart
    st.write('#### Plot Rata-rata Margin pada Usaha Bangkrut dan Tidak Bangkrut')
    fig = px.bar(topmargin, x="Bankrupt?", y=["Operating Gross Margin", "Realized Sales Gross Margin"], orientation='v', text_auto='.2f')
    fig.update_yaxes(title_text="Rata-rata Margin")
    fig.update_xaxes(title_text="Status Bangkrut")
    # display bar chart 
    st.plotly_chart(fig)
    # description
    st.write('Tidak terlihat perbedaan signifikan antara rerata margin pada usaha yang mengalami kebangkrutan dan tidak mengalami kebangkrutan.')

    # create bar chart3
    # grouping by bankrupt and averaging assets
    topasset = df.groupby("Bankrupt?")[['Quick Assets/Total Assets', 'Current Assets/Total Assets', 'Cash/Total Assets']].mean().sort_values(ascending=False, by='Current Assets/Total Assets')
    topasset = topasset.reset_index()
    # bar chart
    st.write('#### Plot Rata-rata Aset pada Usaha Bangkrut dan Tidak Bangkrut')
    fig = px.bar(topasset, x="Bankrupt?", y=['Quick Assets/Total Assets', 'Current Assets/Total Assets', 'Cash/Total Assets'], orientation='v', text_auto='.2f')
    fig.update_yaxes(title_text="Rata-rata Aset")
    fig.update_xaxes(title_text="Status Bangkrut")
    # display bar chart and grouping data
    st.plotly_chart(fig)
    # description
    st.write('Terlihat bahwa perusahaan yang tidak bangkrut memiliki nilai yang lebih tinggi pada rata-rata aset. Perbedaan signifikan ini dapat menandakan bahwa usaha-usaha yang bangkrut mungkin dipengaruhi oleh sedikitnya aset usaha mereka.')

    # create bar chart4
    # grouping by bankrupt and averaging debt
    topdebt = df.groupby("Bankrupt?")['Total debt/Total net worth'].mean().sort_values(ascending=True)
    topdebt = topdebt.reset_index()
    # bar chart Total 
    st.write('#### Plot Rata-rata Total Hutang dibandingkan Total Nilai Kekayaan pada Usaha Bangkrut dan Tidak Bangkrut')
    fig = px.bar(topdebt, x="Bankrupt?", y='Total debt/Total net worth', orientation='v', text_auto='.2s')
    fig.update_yaxes(title_text="Total Hutang/Total Nilai Kekayaan")
    fig.update_xaxes(title_text="Status Bangkrut")
    # display bar chart and grouping data
    st.plotly_chart(fig)
    # description
    st.write('Jelas terlihat perbedaan yang sangat signifikan antara usaha bangkrut dan tidak bangkrut. Pada usaha bangkrut nilai hutang dibanding kekayaan usaha tersebut sangat tinggi, ini dapat saja menjadi salah satu faktor penyebab gagalnya usaha.')

    # create bar chart5
    # grouping by bankrupt and averaging expense
    topexpense = df.groupby("Bankrupt?")['Total expense/Assets'].mean().sort_values(ascending=True)
    topexpense = topexpense.reset_index()
    # bar chart
    st.write('#### Plot Rata-rata Total Pengeluaran dibandingkan Aset pada Usaha Bangkrut dan Tidak Bangkrut')
    fig = px.bar(topexpense, x="Bankrupt?", y='Total expense/Assets', orientation='v', text_auto='.2f')
    fig.update_yaxes(title_text='Total Pengeluaran/Aset')
    fig.update_xaxes(title_text="Status Bangkrut")
    # display bar chart and grouping data
    st.plotly_chart(fig)
    # description
    st.write('Kembali terlihat perbedaan antara usaha bangkrut dan tidak bangkrut. Meskipun skalanya kecil, terlihat bahwa usaha yang bangkrut memiliki pengeluaran berbanding dengan aset yang relatif tinggi jika dilihat dari sisi usaha yang tidak bangkrut.')
    # separator
    st.markdown('---')

    #write
    st.write('#### Exploratory Data Analysis Recap')
    st.write('Dari eksplorasi singkat di atas, terlihat perbedaan cukup signifikan antara data-data usaha yang bangkrut dengan data usaha yang tidak bangkrut. Terlihat pada rata-rata kolom-kolom hutang, aset, dan pengeluaran bahwa usaha bangkrut dengan tidak bangkrut memiliki perbedaan. Untuk mengetahui apakah perbedaan tersebut berkorelasi dengan status kebangkrutan perlu dilakukan analisis korelasi lebih lanjut. Jumlah bangkrut yang sangat rendah dalam dataset dibandingkan usaha yang tidak bangkrut, menandakan bahwa dataset akan perlu dilakukan balancing agar model dapat berfungsi optimal.')

# run app
if __name__ == '__main__':
    run()