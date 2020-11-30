import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from matplotlib import font_manager, rc
import numpy as np
import csv
import seaborn as sns

#한글폰트 적용 - 한글깨짐 방지
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
plt.rcParams['axes.unicode_minus'] = False

# csv파일 읽어오기
df_source = pd.read_csv('NHIS_OPEN_GJ_2017_4.csv', encoding='cp949')
df_source

fig, ax = plt.subplots(figsize=(14, 9))
plt.subplots_adjust(bottom=0.2) # plot 하단에 버튼을 표시할 공간 생성

class Index:
    def 혈당분포(self, event):
	#체중(x), 신장(y) 별 인원 분포
        ax.clear() # ax에 나타난 그래프 내용 초기화

	# pivot테이블
        df_pivot = pd.pivot_table(df_source, index='신장', columns='체중', values='식전혈당', aggfunc='mean')
        #heatmap그래프 - cbar는 clear()이 적용되지 않으므로 사용하지 않았다
        sns.heatmap(df_pivot, cmap='Reds', annot=True, annot_kws={'size':15}, fmt='.1f', ax=ax, cbar=False)

        ax.set_title('체중, 신장 별 평균 혈당 수치 분포', fontsize=20, y=1.05)
        ax.set_xlabel('체중', fontsze=14)
        ax.set_ylabel('신장', fontsize=14)
        ax.set_xticklabels(x_label)
        ax.set_yticklabels(y_label)
        ax.tick_params(axis='x', labelsize=14, length=10, width=3, rotation=0)
        ax.tick_params(axis='y', labelsize=12, length=10, width=3, rotation=30)

        del df_pivot
        plt.draw()

    def 콜레스테롤분포(self, event):
	#상품코드(x), 기업규모(y) 별 기업 평균 매출액 분포
        ax.clear()
	
        df_pivot = pd.pivot_table(df_source, index='신장', columns='체중', values='총콜레스테롤', aggfunc='mean')
        sns.heatmap(df_pivot, cmap='RdBu', annot=True, annot_kws={'size':15}, fmt='.1f', ax=ax, cbar=False)

        ax.set_title('체중, 신장 별 평균 콜레스테롤 수치 분포', fontsize=20, y=1.05)
        ax.set_xlabel('체중', fontsze=14)
        ax.set_ylabel('신장', fontsize=14)
        ax.set_xticklabels(x_label)
        ax.set_yticklabels(y_label)
        ax.tick_params(axis='x', labelsize=14, length=10, width=3, rotation=0)
        ax.tick_params(axis='y', labelsize=12, length=10, width=3, rotation=30)

        del df_pivot
        plt.draw()


callback = Index() #클래스 객체 할당

ax혈당분포 = plt.axes([0.1, 0.05, 0.05, 0.05]) #버튼위치 설정(x축, y축, 너비, 높이)
b혈당분포 = Button(ax혈당분포, '혈당분포') #버튼 생성
b혈당분포.on_clicked(callback.혈당분포) # 버튼 이벤트 헨들러

ax콜레스테롤분포 = plt.axes([0.25, 0.05, 0.08, 0.05])
b콜레스테롤분포 = Button(ax콜레스테롤분포, '콜레스테롤 분포')
b콜레스테롤분포.on_clicked(callback.콜레스테롤분포)

plt.show()
