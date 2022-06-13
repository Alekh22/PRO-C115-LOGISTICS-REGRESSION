import pandas as pd
import plotly.express as px
df = pd.read_csv("escape_velocity.py")
velocity_list = df["Velocity"].tolist()
escaped_list = df["Escaped"].tolist()

fig = px.scatter(x=velocity_list, y=escaped_list)
fig.show()

X = np.reshape(velocity_list,(len(score_list), 1))
Y = np.reshape(escaped_list,(len(accepted), 1))
lr = LogisticRegression()
lr.fit(X,Y)
plt.figure()
plt.scater(X.ravel(),Y, culor="Black",zorder=20)
def model(x):
    return 1/(1+np.exp(-x))
X_test = np.linspace(0, 100, 200)
chances = model(X_test * lr.coef_ + lr.intercept_).ravel()
plt.plot(X_test, chances, color='red', linewidth=3)
plt.axhline(y=0, color='k', linestyle='-')
plt.axhline(y=1, color='k', linestyle='-')
plt.axhline(y=0.5, color='b', linestyle='--')

# do hit and trial by changing the value of X_test
plt.axvline(x=X_test[165], color='b', linestyle='--')

plt.ylabel('y')
plt.xlabel('X')
plt.xlim(75, 85)
plt.show()
