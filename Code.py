import pandas as pd
import regex as re
import matplotlib.pyplot as plt
import seaborn as sns

df_NYG = pd.read_html('https://en.wikipedia.org/wiki/List_of_New_York_Giants_seasons')
df_NYJ = pd.read_html('https://en.wikipedia.org/wiki/List_of_New_York_Jets_seasons')
df_NYG = df_NYG[3]
df_NYJ = df_NYJ[1]

#Cleaning Data
df_NYG.columns = [' '.join(col).strip() for col in df_NYG.columns.values]
df_NYG_loss = df_NYG_filtered['Regular season']['L']
df_NYG_tie = df_NYG_filtered['Regular season']['T']
df_NYG_win = df_NYG_filtered['Regular season']['.mw-parser-output .tooltip-dotted{border-bottom:1px dotted;cursor:help}W']
df_NYG_selected = df_NYG[['Season Season', 'Regular season .mw-parser-output .tooltip-dotted{border-bottom:1px dotted;cursor:help}W', 'Regular season L', 'Regular season T']]
df_NYG_selected.columns = ['Season', 'W', 'L', 'T']
df_NYG_selected['Season'] = df_NYG_selected['Season'].astype(str).str.replace(r'\[.*\]', '', regex=True)
df_NYG_selected['Season'] = pd.to_numeric(df_NYG_selected['Season'], errors='coerce')
df_NYG_selected = df_NYG_selected[df_NYG_selected['Season'] >= 2005]
df_NYG_selected.reset_index(inplace = True)
df_NYG_selected.drop(columns=['index'], inplace = True)

df_NYJ.columns = [' '.join(col).strip() for col in df_NYJ.columns.values]
df_NYJ_selected = df_NYJ[['Season Season', 'Regular season .mw-parser-output .tooltip-dotted{border-bottom:1px dotted;cursor:help}W', 'Regular season L', 'Regular season T']]
df_NYJ_selected.columns = ['Season', 'W', 'L', 'T']
df_NYJ_selected['Season'] = df_NYJ_selected['Season'].astype(str).str.replace(r'\[.*\]', '', regex=True)
df_NYJ_selected['Season'] = pd.to_numeric(df_NYJ_selected['Season'], errors='coerce')
df_NYJ_selected = df_NYJ_selected[df_NYJ_selected['Season'] >= 2005]
df_NYJ_selected.reset_index(inplace = True)
df_NYJ_selected.drop(columns=['index'], inplace = True)


#Creating Graph
def convert_to_numeric(df):
    df[["W", "L", "T"]] = df[["W", "L", "T"]].apply(pd.to_numeric, errors="coerce")

def compute_win_percentage(df):
    df["Total Games"] = df["W"] + df["L"] + df["T"]
    df["Win Percentage"] = (df["W"] / df["Total Games"]) * 100 
    return df

convert_to_numeric(df_NYG_selected)
convert_to_numeric(df_NYJ_selected)

df_NYG_selected = compute_win_percentage(df_NYG_selected)
df_NYJ_selected = compute_win_percentage(df_NYJ_selected)

plt.figure(figsize=(12, 6))

plt.plot(df_NYG_selected["Season"], df_NYG_selected["Win Percentage"], label="NYG Win %", color="blue", linestyle="-", marker="o")

plt.plot(df_NYJ_selected["Season"], df_NYJ_selected["Win Percentage"], label="NYJ Win %", color="green", linestyle="--", marker="x")

plt.title("Win Percentage: NY Giants vs. NY Jets", fontsize=14, fontweight="bold")
plt.xlabel("Season", fontsize=12)
plt.ylabel("Win Percentage (%)", fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.show()
