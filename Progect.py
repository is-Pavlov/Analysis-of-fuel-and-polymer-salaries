import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#streamlit run f.py

st.title("Нефтехимия и полимеры")
st.write("В данный момент я получаю высшее химическое образование 	:test_tube::male-student::male-scientist:. Пару лет назад мне предстояло выбрать кафедру для дальнейшего обучения. Я выбирал между нефтехимией :oil_drum: и кафедрой высокомолекулярных соединений :dna:. За основу своего анализа я решил взять изменение зарплат именно в этих отраслях")

oil = Image.open('нефть.jpg')
st.image(oil, caption='Нефтяная вышка')

st.header("Импорт таблицы изменения зарплат без учета инфляции")
df = pd.read_excel("отрасли.xlsx")
st.write(df)
df_t = df.T # Транспонирование таблицы
x = df_t.index[1: ] # Ось х - годы
oil = 0 # Значения производства топлива
df_t_oil = df_t[oil]
y_oil = df_t_oil.values[1:]
pl = 1 # Значения производства пластмасс
df_t_pl = df_t[pl]
y_pl = df_t_pl.values[1:]
st.header('Построение графика изменения зарплат по годам без учета инфляции')
plt.plot(x, y_oil, label = 'производство кокса и нефтепродуктов без учета инфляции', marker = "o") # Настройка графика
plt.plot(x, y_pl, label = 'производство резиновых и  пластмассовых изделий без учета инфляции', marker = "^")
plt.title('Изменение зарплат с 2000 по 2023 год без учета инфляции')
plt.xlabel('Год')
plt.ylabel('Зарплата, руб/мес')
plt.legend()
st.pyplot(plt.gcf())
st.write("Как мы видим, зарплаты в :blue[нефтехимической промышленности] всегда были значительно выше (примерно в 2 раза), чем в аналогичное время на :orange[производстве полимеров]. Так в некоторые года зарплата в :blue[нефтехимии] выше более чем **в 3 раза**. Для :orange[оранжевого] графика характерен плавный рост на протяжении всего промежутка рассматриваемого времени, резкие взлеты и падения отсутсвуют В :blue[нефтехимии] дела обстоят интереснее: на :blue[синем] графике более крутую динамику изменнений. Также рост не постоянен: в 2018, 2019 и 2020 годах наблюдался **спад** :chart_with_downwards_trend: зарплат впревые за **20 лет**.")
st.header('Выводы')
st.write('Предварительно можем сделать вывод, что зарплаты в :orange[полимерной промышленности] являеются более стабильными, в то время, как в :blue[нефтехимической отрасли] они '
         '1) быстрее изменяются; '
         '2) могут не только расти, но и падать')
st.header('Импорт таблицы изменения инфляции')
df_inf = pd.read_excel('Инфляция 2000-2023.xlsx')
st.write(df_inf)
st.write('Здесь нам нужен только столбец с годовой инфляцией и непосредственно год. Создадим таблицу изменения зарплат в :blue[нефтехимии] и :orange[полимерной промышленности] с учетом :yellow[инфляции]')
st.header('Таблица изменения зарплат с учетом инфляции')
df_real = pd.DataFrame({'Год': x, 'производство кокса и нефтепродуктов': y_oil * (1 - 0.01 * df_inf['Всего']), 'производство резиновых и  пластмассовых изделий': y_pl * (1 - 0.01 * df_inf['Всего'])})
st.write(df_real)
st.header('Построение графика изменения зарплат по годам c учетом инфляции')

x_real = df_real['Год']
y_oil_real = df_real['производство кокса и нефтепродуктов']
y_pl_real = df_real['производство резиновых и  пластмассовых изделий']
plt.plot(x_real, y_oil_real, label = 'производство кокса и нефтепродуктов c учетом инфляции', marker = "o") # Настройка графика
plt.plot(x_real, y_pl_real, label = 'производство резиновых и  пластмассовых изделий с учетом инфляции', marker = "^")
plt.title('Изменение зарплат с 2000 по 2023 год с учетом инфляции')
plt.xlabel('Год')
plt.ylabel('Зарплата, руб/мес')
plt.legend()
st.pyplot(plt.gcf())

st.write('Графики изменения зарплат с учетом инфляции и без нее схожи.'
         ' В целом, в нефтехимии разницы почти нет, самые серьезные влияние на зарплату инфляция оказывала в 2014-2015 годах, а также в 2021-2023 годах.'
         ' С зарплатами на полимерных производствах дела обстоят еще лучше. Немного больше, чем обычно, инфляция сыграла в 2014-2015 и в 2021-2023 годах. Но из-за того, что зарплаты на полимерных предприятиях в целом ниже, чем на нефтехимических, инфляция меньше влияет на абсолютные числа.')
st.header('Вывод')
st.write('Первое, что я бы хотел отметить, это разницу в зарплатах: нефтехимическая отрасль в нашей стране ценится гораздо больше (а именно в 2-3 раза!), чем деятельность, связанная с пластмассами и эластомерами. Графики изменения зарплат без учета инфляции ведут себя схожим образом с графиками с учетом инфляции: наблюдается плавный рост. Если же рассматривать каждую промышленность по отдельности, то можем заменить, что больше всего инфляция сказывалась на зарплате в 2014-2015 и в 2021-2023 годах. Предполагаю, что спады могут быть вызваны неоднозначной реакцией на внешнюю политику нашей страны на международной арене. ')

