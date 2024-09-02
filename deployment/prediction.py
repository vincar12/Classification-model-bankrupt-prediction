# import library
import streamlit as st
import pickle
import pandas as pd

# load files
with open('model.pkl', 'rb') as file:
  model = pickle.load(file)

def run():
  # create title
  st.title('Cek Prediksi Bangkrut')

  # create form
  with st.form('form_finansial'):
    # title
    st.write('#### Form Finansial')

    # columns for input
    ROAC_before_interest = st.number_input('Pengembalian aset(C) sebelum bunga dan depresiasi sebelum bunga', min_value=0.0, value=0.5, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    ROAA_before_interest = st.number_input('Pengembalian aset(A) sebelum bunga dan % setelah pajak', min_value=0.0, value=0.5, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    ROAB_before_interest = st.number_input('Pengembalian aset(B) sebelum bunga dan depresiasi setelah pajak', min_value=0.0, value=0.5, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Operating_Gross_Margin = st.number_input('Margin Kotor Operasional', min_value=0.0, value=0.5, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Realized_Sales_Gross_Margin = st.number_input('Margin Kotor Penjualan Terealisasi', min_value=0.0, value=0.5, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Operating_Profit_Rate = st.number_input('Tingkat Laba Operasional', min_value=0.0, value=0.9, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Pretax_net_Interest_Rate = st.number_input('Tingkat Bunga Bersih Sebelum Pajak', min_value=0.0, value=0.8, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Aftertax_net_Interest_Rate = st.number_input('Tingkat Bunga Bersih Setelah Pajak', min_value=0.0, value=0.8, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    # separator
    st.markdown('---')
    Nonindustry_income = st.number_input('Pendapatan dan Pengeluaran Non-industri/Pendapatan', min_value=0.0, value=0.3, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Continuous_interest_rate = st.number_input('Tingkat Bunga Kontinu (setelah pajak)', min_value=0.0, value=0.8, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Operating_Expense_Rate = st.number_input('Tingkat Beban Operasional', min_value=0.0, value=0.0003, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Research_and_development_expense_rate = st.number_input('Tingkat Beban Penelitian dan Pengembangan', min_value=0.0, value=5000000000.0, max_value=10000000000.0, help='Isi dengan angka, cth. 1000. Minimum = 0, Maximum = 10000000000')
    Cash_flow_rate = st.number_input('Tingkat Arus Kas', min_value=0.0, value=0.5, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Interest_bearing_debt_interest_rate = st.number_input('Tingkat Bunga Hutang Berbunga', min_value=0.0, value=0.0008, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Tax_rate_A = st.number_input('Tarif Pajak (A)', min_value=0.0, value=0.2, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    # separator
    st.markdown('---')
    Net_Value_Per_Share_B = st.number_input('Nilai Bersih Per Saham (B)', min_value=0.0, value=0.15, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Net_Value_Per_Share_A = st.number_input('Nilai Bersih Per Saham (A)', min_value=0.0, value=0.15, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Net_Value_Per_Share_C = st.number_input('Nilai Bersih Per Saham (C)', min_value=0.0, value=0.15, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Persistent_EPS_in_the_Last_Four_Seasons = st.number_input('EPS Persisten dalam Empat Musim Terakhir', min_value=0.0, value=0.2, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Cash_Flow_Per_Share = st.number_input('Arus Kas Per Saham', min_value=0.0, value=0.3, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Revenue_Per_Share = st.number_input('Pendapatan Per Saham (Yuan ¥)', min_value=0.0, value=0.05, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Operating_Profit_Per_Share = st.number_input('Laba Operasional Per Saham (Yuan ¥)', min_value=0.0, value=0.1, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Per_Share_Net_profit_before_tax = st.number_input('Laba Bersih Per Saham Sebelum Pajak (Yuan ¥)', min_value=0.0, value=0.1, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    # separator
    st.markdown('---')
    Realized_Sales_Gross_Profit_Growth_Rate = st.number_input('Tingkat Pertumbuhan Laba Kotor Penjualan Terealisasi', min_value=0.0, value=0.02, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Operating_Profit_Growth_Rate = st.number_input('Tingkat Pertumbuhan Laba Operasional', min_value=0.0, value=0.8, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    After_tax_Net_Profit_Growth_Rate = st.number_input('Tingkat Pertumbuhan Laba Bersih Setelah Pajak', min_value=0.0, value=0.6, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Regular_Net_Profit_Growth_Rate = st.number_input('Tingkat Pertumbuhan Laba Bersih Reguler', min_value=0.0, value=0.7, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Continuous_Net_Profit_Growth_Rate = st.number_input('Tingkat Pertumbuhan Laba Bersih Kontinu', min_value=0.0, value=0.2, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Total_Asset_Growth_Rate = st.number_input('Tingkat Pertumbuhan Total Aset', min_value=0.0, value=500000000.0, max_value=10000000000.0, help='Isi dengan angka, cth. 5000. Minimum = 0, Maximum = 10000000000')
    Net_Value_Growth_Rate = st.number_input('Tingkat Pertumbuhan Nilai Bersih', min_value=0.0, value=0.0004, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Total_Asset_Return_Growth_Rate_Ratio = st.number_input('Rasio Pertumbuhan Pengembalian Total Aset', min_value=0.0, value=0.2, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Cash_Reinvestment_Percent = st.number_input('Persentase Investasi Kembali Kas', min_value=0.0, value=0.3, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    # separator
    st.markdown('---')
    Current_Ratio = st.number_input('Rasio Lancar', min_value=0.0, value=0.01, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Quick_Ratio = st.number_input('Rasio Cepat', min_value=0.0, value=0.001, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Interest_Expense_Ratio = st.number_input('Rasio Beban Bunga', min_value=0.0, value=0.6, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Total_debt_Total_net_worth = st.number_input('Total Hutang/Total Kekayaan Bersih', min_value=0.0, value=0.01, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Debt_ratio_Percent = st.number_input('Rasio Hutang %', min_value=0.0, value=0.1, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Net_worth_Assets = st.number_input('Kekayaan Bersih/Aset', min_value=0.0, value=0.8, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Long_term_fund_suitability_ratio_A = st.number_input('Rasio Kecocokan Dana Jangka Panjang (A)', min_value=0.0, value=0.005, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Borrowing_dependency = st.number_input('Ketergantungan Pinjaman', min_value=0.0, value=0.3, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Contingent_liabilities_Net_worth = st.number_input('Kewajiban Kontinjensi/Kekayaan Bersih', min_value=0.0, value=0.006, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Operating_profit_Paid_in_capital = st.number_input('Laba Operasional/Modal Disetor', min_value=0.0, value=0.1, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Net_profit_before_tax_Paid_in_capital = st.number_input('Laba Bersih Sebelum Pajak/Modal Disetor', min_value=0.0, value=0.1, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Inventory_and_accounts_receivable_Net_value = st.number_input('Inventaris dan Piutang/Net Value', min_value=0.0, value=0.4, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    # separator
    st.markdown('---')
    Total_Asset_Turnover = st.number_input('Perputaran Total Aset', min_value=0.0, value=0.5, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Accounts_Receivable_Turnover = st.number_input('Perputaran Piutang', min_value=0.0, value=0.1, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Average_Collection_Days = st.number_input('Hari Rata-rata Penagihan', min_value=0.0, value=0.001, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Inventory_Turnover_Rate_times = st.number_input('Tingkat Perputaran Persediaan (kali)', min_value=0.0, value=0.0001, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Fixed_Assets_Turnover_Frequency = st.number_input('Frekuensi Perputaran Aset Tetap', min_value=0.0, value=0.0001, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Net_Worth_Turnover_Rate_times = st.number_input('Tingkat Perputaran Kekayaan Bersih (kali)', min_value=0.0, value=0.02, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Revenue_per_person = st.number_input('Pendapatan per Orang', min_value=0.0, value=0.03, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Operating_profit_per_person = st.number_input('Laba Operasional per Orang', min_value=0.0, value=0.4, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Allocation_rate_per_person = st.number_input('Tingkat Alokasi per Orang', min_value=0.0, value=0.01, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Working_Capital_to_Total_Assets = st.number_input('Modal Kerja terhadap Total Aset', min_value=0.0, value=0.7, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Quick_Assets_Total_Assets = st.number_input('Aset Cepat/Total Aset', min_value=0.0, value=0.2, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Current_Assets_Total_Assets = st.number_input('Aset Lancar/Total Aset', min_value=0.0, value=0.3, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Cash_Total_Assets = st.number_input('Kas/Total Aset', min_value=0.0, value=0.05, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    # separator
    st.markdown('---')
    Quick_Assets_Current_Liability = st.number_input('Aset Cepat/Kewajiban Lancar', min_value=0.0, value=0.005, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Cash_Current_Liability = st.number_input('Kas/Kewajiban Lancar', min_value=0.0, value=0.005, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Current_Liability_to_Assets = st.number_input('Kewajiban Lancar terhadap Aset', min_value=0.0, value=0.05, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Operating_Funds_to_Liability = st.number_input('Dana Operasional terhadap Kewajiban', min_value=0.0, value=0.3, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Inventory_Working_Capital = st.number_input('Persediaan/Modal Kerja', min_value=0.0, value=0.2, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Inventory_Current_Liability = st.number_input('Persediaan/Kewajiban Lancar', min_value=0.0, value=0.005, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Current_Liabilities_Liability = st.number_input('Kewajiban Lancar/Kewajiban', min_value=0.0, value=0.5, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Working_Capital_Equity = st.number_input('Modal Kerja/Equitas', min_value=0.0, value=0.7, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Current_Liabilities_Equity = st.number_input('Kewajiban Lancar/Equitas', min_value=0.0, value=0.3, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Long_term_Liability_Current_Assets = st.number_input('Kewajiban Jangka Panjang terhadap Aset Lancar', min_value=0.0, value=0.005, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Retained_Earnings_Total_Assets = st.number_input('Laba Ditahan terhadap Total Aset', min_value=0.0, value=0.9, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Total_income_Total_expense = st.number_input('Total Pendapatan/Total Beban', min_value=0.0, value=0.002, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Total_expense_Assets = st.number_input('Total Beban/Aset', min_value=0.0, value=0.05, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Current_Asset_Turnover_Rate = st.number_input('Tingkat Perputaran Aset Lancar', min_value=0.0, value=1000000000.0, max_value=10000000000.0, help='Isi dengan angka, cth. 567. Minimum = 0, Maximum = 10000000000')
    Quick_Asset_Turnover_Rate = st.number_input('Tingkat Perputaran Aset Cepat', min_value=0.0, value=2000000000.0, max_value=10000000000.0, help='Isi dengan angka, cth. 567. Minimum = 0, Maximum = 10000000000')
    Working_capital_Turnover_Rate = st.number_input('Tingkat Perputaran Modal Kerja', min_value=0.0, value=0.5, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Cash_Turnover_Rate = st.number_input('Tingkat Perputaran Kas', min_value=0.0, value=2000000000.0, max_value=10000000000.0, help='Isi dengan angka, cth. 567. Minimum = 0, Maximum = 10000000000')
    Cash_Flow_to_Sales = st.number_input('Arus Kas terhadap Penjualan', min_value=0.0, value=0.6, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    # separator
    st.markdown('---')
    Fixed_Assets_to_Assets = st.number_input('Aset Tetap terhadap Aset', min_value=0.0, value=0.3, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Current_Liability_to_Liability = st.number_input('Kewajiban Lancar terhadap Kewajiban', min_value=0.0, value=0.5, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Current_Liability_to_Equity = st.number_input('Kewajiban Lancar terhadap Equitas', min_value=0.0, value=0.3, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Equity_to_Long_term_Liability = st.number_input('Equitas terhadap Kewajiban Jangka Panjang', min_value=0.0, value=0.1, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Cash_Flow_to_Total_Assets = st.number_input('Arus Kas terhadap Total Aset', min_value=0.0, value=0.6, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Cash_Flow_to_Liability = st.number_input('Arus Kas terhadap Kewajiban', min_value=0.0, value=0.4, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    CFO_to_Assets = st.number_input('CFO terhadap Aset', min_value=0.0, value=0.5, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Cash_Flow_to_Equity = st.number_input('Arus Kas terhadap Equitas', min_value=0.0, value=0.3, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Current_Liability_to_Current_Assets = st.number_input('Kewajiban Lancar terhadap Aset Lancar', min_value=0.0, value=0.03, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Liability_Assets_Flag = st.selectbox('Bendera Kewajiban-Aset', (0, 1), index=0, help='Pilih angka yang sesuai. Aset Lebih dari Kewajiban = 0, Kewajiban Lebih dari Aset = 1')
    # separator
    st.markdown('---')
    Net_Income_to_Total_Assets = st.number_input('Pendapatan Bersih terhadap Total Aset', min_value=0.0, value=0.8, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Total_assets_to_GNP_price = st.number_input('Total Aset terhadap Harga PNB', min_value=0.0, value=0.005, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    No_credit_Interval = st.number_input('Interval Tanpa Kredit', min_value=0.0, value=0.6, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Gross_Profit_to_Sales = st.number_input('Laba Kotor terhadap Penjualan', min_value=0.0, value=0.6, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Net_Income_to_Stockholders_Equity = st.number_input('Pendapatan Bersih terhadap Ekuitas Pemegang Saham', min_value=0.0, value=0.8, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Liability_to_Equity = st.number_input('Kewajiban terhadap Equitas', min_value=0.0, value=0.3, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Degree_of_Financial_Leverage_DFL = st.number_input('Tingkat Leverage Keuangan (DFL)', min_value=0.0, value=0.02, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Interest_Coverage_Ratio_Interest_expense_to_EBIT = st.number_input('Rasio Cakupan Bunga (Beban bunga terhadap EBIT)', min_value=0.0, value=0.5, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    Net_Income_Flag = st.selectbox('Bendera Kewajiban-Aset', (0, 1), index=1, help='Pilih angka yang sesuai. Pendapatan Bersih Lebih dari Kerugian Bersih = 0, Pendapatan Bersih Kurang dari Kerugian Bersih = 1')
    Equity_to_Liability = st.number_input('Equitas terhadap Kewajiban', min_value=0.0, value=0.03, max_value=1.0, help='Isi dengan angka rasio, cth. 0.567. Minimum = 0, Maximum = 1')
    
    # submit button
    submitted = st.form_submit_button('Cek Prediksi Bangkrut')

  # input data from form into table
  data_inf = {
    "ROA(C) before interest and depreciation before interest" : ROAC_before_interest,
    "ROA(A) before interest and % after tax" : ROAA_before_interest,
    "ROA(B) before interest and depreciation after tax" : ROAB_before_interest,
    "Operating Gross Margin" : Operating_Gross_Margin, 
    "Realized Sales Gross Margin" : Realized_Sales_Gross_Margin,
    "Operating Profit Rate" : Operating_Profit_Rate, 
    "Pre-tax net Interest Rate" : Pretax_net_Interest_Rate,
    "After-tax net Interest Rate" : Aftertax_net_Interest_Rate,
    "Non-industry income and expenditure/revenue" : Nonindustry_income,
    "Continuous interest rate (after tax)" : Continuous_interest_rate, 
    "Operating Expense Rate" : Operating_Expense_Rate,
    "Research and development expense rate" : Research_and_development_expense_rate, 
    "Cash flow rate" : Cash_flow_rate,
    "Interest-bearing debt interest rate" : Interest_bearing_debt_interest_rate, 
    "Tax rate (A)" : Tax_rate_A,
    "Net Value Per Share (B)" : Net_Value_Per_Share_B, 
    "Net Value Per Share (A)" : Net_Value_Per_Share_A,
    "Net Value Per Share (C)" : Net_Value_Per_Share_C, 
    "Persistent EPS in the Last Four Seasons" : Persistent_EPS_in_the_Last_Four_Seasons,
    "Cash Flow Per Share" : Cash_Flow_Per_Share, 
    "Revenue Per Share (Yuan ¥)" : Revenue_Per_Share,
    "Operating Profit Per Share (Yuan ¥)" : Operating_Profit_Per_Share,
    "Per Share Net profit before tax (Yuan ¥)" : Per_Share_Net_profit_before_tax,
    "Realized Sales Gross Profit Growth Rate" : Realized_Sales_Gross_Profit_Growth_Rate,
    "Operating Profit Growth Rate" : Operating_Profit_Growth_Rate, 
    "After-tax Net Profit Growth Rate" : After_tax_Net_Profit_Growth_Rate,
    "Regular Net Profit Growth Rate" : Regular_Net_Profit_Growth_Rate, 
    "Continuous Net Profit Growth Rate" : Continuous_Net_Profit_Growth_Rate,
    "Total Asset Growth Rate" : Total_Asset_Growth_Rate, 
    "Net Value Growth Rate" : Net_Value_Growth_Rate,
    "Total Asset Return Growth Rate Ratio" : Total_Asset_Return_Growth_Rate_Ratio, 
    "Cash Reinvestment %" : Cash_Reinvestment_Percent,
    "Current Ratio" : Current_Ratio, 
    "Quick Ratio" : Quick_Ratio, 
    "Interest Expense Ratio" : Interest_Expense_Ratio,
    "Total debt/Total net worth" : Total_debt_Total_net_worth, 
    "Debt ratio %" : Debt_ratio_Percent, 
    "Net worth/Assets" : Net_worth_Assets,
    "Long-term fund suitability ratio (A)" : Long_term_fund_suitability_ratio_A, 
    "Borrowing dependency" : Borrowing_dependency,
    "Contingent liabilities/Net worth" : Contingent_liabilities_Net_worth, 
    "Operating profit/Paid-in capital" : Operating_profit_Paid_in_capital,
    "Net profit before tax/Paid-in capital" : Net_profit_before_tax_Paid_in_capital,
    "Inventory and accounts receivable/Net value" : Inventory_and_accounts_receivable_Net_value, 
    "Total Asset Turnover" : Total_Asset_Turnover,
    "Accounts Receivable Turnover" : Accounts_Receivable_Turnover, 
    "Average Collection Days" : Average_Collection_Days,
    "Inventory Turnover Rate (times)" : Inventory_Turnover_Rate_times, 
    "Fixed Assets Turnover Frequency" : Fixed_Assets_Turnover_Frequency,
    "Net Worth Turnover Rate (times)" : Net_Worth_Turnover_Rate_times, 
    "Revenue per person" : Revenue_per_person,
    "Operating profit per person" : Operating_profit_per_person, 
    "Allocation rate per person" : Allocation_rate_per_person,
    "Working Capital to Total Assets" : Working_Capital_to_Total_Assets, 
    "Quick Assets/Total Assets" : Quick_Assets_Total_Assets,
    "Current Assets/Total Assets" : Current_Assets_Total_Assets, 
    "Cash/Total Assets" : Cash_Total_Assets,
    "Quick Assets/Current Liability" : Quick_Assets_Current_Liability, 
    "Cash/Current Liability" : Cash_Current_Liability,
    "Current Liability to Assets" : Current_Liability_to_Assets, 
    "Operating Funds to Liability" : Operating_Funds_to_Liability,
    "Inventory/Working Capital" : Inventory_Working_Capital, 
    "Inventory/Current Liability" : Inventory_Current_Liability,
    "Current Liabilities/Liability" : Current_Liabilities_Liability, 
    "Working Capital/Equity" : Working_Capital_Equity,
    "Current Liabilities/Equity" : Current_Liabilities_Equity, 
    "Long-term Liability to Current Assets" : Long_term_Liability_Current_Assets,
    "Retained Earnings to Total Assets" : Retained_Earnings_Total_Assets, 
    "Total income/Total expense" : Total_income_Total_expense,
    "Total expense/Assets" : Total_expense_Assets, 
    "Current Asset Turnover Rate" : Current_Asset_Turnover_Rate,
    "Quick Asset Turnover Rate" : Quick_Asset_Turnover_Rate, 
    "Working capitcal Turnover Rate" : Working_capital_Turnover_Rate,
    "Cash Turnover Rate" : Cash_Turnover_Rate, 
    "Cash Flow to Sales" : Cash_Flow_to_Sales, 
    "Fixed Assets to Assets" : Fixed_Assets_to_Assets,
    "Current Liability to Liability" : Current_Liability_to_Liability, 
    "Current Liability to Equity" : Current_Liability_to_Equity,
    "Equity to Long-term Liability" : Equity_to_Long_term_Liability, 
    "Cash Flow to Total Assets" : Cash_Flow_to_Total_Assets,
    "Cash Flow to Liability" : Cash_Flow_to_Liability, 
    "CFO to Assets" : CFO_to_Assets, 
    "Cash Flow to Equity" : Cash_Flow_to_Equity,
    "Current Liability to Current Assets" : Current_Liability_to_Current_Assets, 
    "Liability-Assets Flag" : Liability_Assets_Flag,
    "Net Income to Total Assets" : Net_Income_to_Total_Assets, 
    "Total assets to GNP price" : Total_assets_to_GNP_price,
    "No-credit Interval" : No_credit_Interval, 
    "Gross Profit to Sales" : Gross_Profit_to_Sales,
    "Net Income to Stockholder's Equity" : Net_Income_to_Stockholders_Equity, 
    "Liability to Equity" : Liability_to_Equity,
    "Degree of Financial Leverage (DFL)" : Degree_of_Financial_Leverage_DFL,
    "Interest Coverage Ratio (Interest expense to EBIT)" : Interest_Coverage_Ratio_Interest_expense_to_EBIT, 
    "Net Income Flag" : Net_Income_Flag,
    "Equity to Liability" : Equity_to_Liability}
  
  # create dataframe
  data_inf = pd.DataFrame([data_inf])
  st.dataframe(data_inf)

  if submitted:
    # predict using model
    y_pred_inf = model.predict(data_inf)
    rating_desc = 'Tidak Diprediksi Bangkrut' if y_pred_inf[0] == 0 else 'Diprediksi Bangkrut'
    # display prediction result
    st.write('### Prediksi Kebangkrutan :', str(int(y_pred_inf)), '-', rating_desc)

# run app
if __name__ == '__main__':
  run()