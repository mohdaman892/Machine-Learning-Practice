{"metadata":{"kernelspec":{"language":"python","display_name":"Python 3","name":"python3"},"language_info":{"name":"python","version":"3.10.13","mimetype":"text/x-python","codemirror_mode":{"name":"ipython","version":3},"pygments_lexer":"ipython3","nbconvert_exporter":"python","file_extension":".py"},"kaggle":{"accelerator":"none","dataSources":[{"sourceId":5845248,"sourceType":"datasetVersion","datasetId":3360797}],"dockerImageVersionId":30732,"isInternetEnabled":false,"language":"python","sourceType":"script","isGpuEnabled":false}},"nbformat_minor":4,"nbformat":4,"cells":[{"cell_type":"code","source":"# %% [code] {\"execution\":{\"iopub.status.busy\":\"2024-06-30T08:45:06.673719Z\",\"iopub.execute_input\":\"2024-06-30T08:45:06.674144Z\",\"iopub.status.idle\":\"2024-06-30T08:45:07.120870Z\",\"shell.execute_reply.started\":\"2024-06-30T08:45:06.674110Z\",\"shell.execute_reply\":\"2024-06-30T08:45:07.119765Z\"},\"jupyter\":{\"outputs_hidden\":false}}\n# This Python 3 environment comes with many helpful analytics libraries installed\n# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python\n# For example, here's several helpful packages to load\n\nimport numpy as np # linear algebra\nimport pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)\n\n# Input data files are available in the read-only \"../input/\" directory\n# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory\n\nimport os\nfor dirname, _, filenames in os.walk('/kaggle/input'):\n    for filename in filenames:\n        print(os.path.join(dirname, filename))\n\n# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using \"Save & Run All\" \n# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session\n\n# %% [code] {\"execution\":{\"iopub.status.busy\":\"2024-06-30T08:45:07.122928Z\",\"iopub.execute_input\":\"2024-06-30T08:45:07.123928Z\",\"iopub.status.idle\":\"2024-06-30T08:45:07.155292Z\",\"shell.execute_reply.started\":\"2024-06-30T08:45:07.123894Z\",\"shell.execute_reply\":\"2024-06-30T08:45:07.154191Z\"},\"jupyter\":{\"outputs_hidden\":false}}\ndf = pd.read_csv(\"/kaggle/input/salary-prediction-data-simple-linear-regression/Salary_Data.csv\")\nprint(df.head())\n\n# %% [code] {\"execution\":{\"iopub.status.busy\":\"2024-06-30T08:45:07.156766Z\",\"iopub.execute_input\":\"2024-06-30T08:45:07.157207Z\",\"iopub.status.idle\":\"2024-06-30T08:45:07.972602Z\",\"shell.execute_reply.started\":\"2024-06-30T08:45:07.157169Z\",\"shell.execute_reply\":\"2024-06-30T08:45:07.971404Z\"},\"jupyter\":{\"outputs_hidden\":false}}\nfrom sklearn.linear_model import LinearRegression\nimport matplotlib.pyplot as plt\n\n# %% [code] {\"execution\":{\"iopub.status.busy\":\"2024-06-30T08:45:07.974530Z\",\"iopub.execute_input\":\"2024-06-30T08:45:07.975020Z\",\"iopub.status.idle\":\"2024-06-30T08:45:07.983004Z\",\"shell.execute_reply.started\":\"2024-06-30T08:45:07.974961Z\",\"shell.execute_reply\":\"2024-06-30T08:45:07.981635Z\"},\"jupyter\":{\"outputs_hidden\":false}}\nx_train = np.array([[x] for x in df[\"YearsExperience\"]]) \ny_train = np.array(df[\"Salary\"])\nprint(y_train)\n\n# %% [code] {\"execution\":{\"iopub.status.busy\":\"2024-06-30T08:45:07.987382Z\",\"iopub.execute_input\":\"2024-06-30T08:45:07.988239Z\",\"iopub.status.idle\":\"2024-06-30T08:45:08.327552Z\",\"shell.execute_reply.started\":\"2024-06-30T08:45:07.988190Z\",\"shell.execute_reply\":\"2024-06-30T08:45:08.326267Z\"},\"jupyter\":{\"outputs_hidden\":false}}\nplt.scatter(df[\"YearsExperience\"],y_train,color=\"red\")\nplt.xlabel(\"YOE in years\")\nplt.ylabel(\"Salary\")\n\n# %% [code] {\"execution\":{\"iopub.status.busy\":\"2024-06-30T08:45:08.329140Z\",\"iopub.execute_input\":\"2024-06-30T08:45:08.329554Z\",\"iopub.status.idle\":\"2024-06-30T08:45:08.347621Z\",\"shell.execute_reply.started\":\"2024-06-30T08:45:08.329519Z\",\"shell.execute_reply\":\"2024-06-30T08:45:08.346213Z\"},\"jupyter\":{\"outputs_hidden\":false}}\nreg = LinearRegression().fit(x_train, y_train)\n\n# %% [code] {\"execution\":{\"iopub.status.busy\":\"2024-06-30T08:45:08.349145Z\",\"iopub.execute_input\":\"2024-06-30T08:45:08.349559Z\",\"iopub.status.idle\":\"2024-06-30T08:45:08.362901Z\",\"shell.execute_reply.started\":\"2024-06-30T08:45:08.349524Z\",\"shell.execute_reply\":\"2024-06-30T08:45:08.361673Z\"},\"jupyter\":{\"outputs_hidden\":false}}\nreg.score(x_train, y_train)\n\n# %% [code] {\"execution\":{\"iopub.status.busy\":\"2024-06-30T08:45:08.364500Z\",\"iopub.execute_input\":\"2024-06-30T08:45:08.365035Z\",\"iopub.status.idle\":\"2024-06-30T08:45:08.373736Z\",\"shell.execute_reply.started\":\"2024-06-30T08:45:08.364975Z\",\"shell.execute_reply\":\"2024-06-30T08:45:08.372444Z\"},\"jupyter\":{\"outputs_hidden\":false}}\n# Line Eqn = wx+b\nw, b = reg.coef_[0], reg.intercept_\nx_line = []\nx_line.append((y_train[0] - b) / w)\nx_line.append((y_train[-1] - b) / w)\ny_line = [y_train[0],y_train[-1]]\n\n# %% [code] {\"execution\":{\"iopub.status.busy\":\"2024-06-30T08:45:08.375269Z\",\"iopub.execute_input\":\"2024-06-30T08:45:08.375971Z\",\"iopub.status.idle\":\"2024-06-30T08:45:08.673564Z\",\"shell.execute_reply.started\":\"2024-06-30T08:45:08.375930Z\",\"shell.execute_reply\":\"2024-06-30T08:45:08.671563Z\"},\"jupyter\":{\"outputs_hidden\":false}}\nplt.scatter(df[\"YearsExperience\"],y_train,color=\"red\")\nplt.plot(x_line, y_line,color=\"blue\")\nplt.xlabel(\"YOE in years\")\nplt.ylabel(\"Salary\")\n\n# %% [code] {\"execution\":{\"iopub.status.busy\":\"2024-06-30T08:45:08.675033Z\",\"iopub.execute_input\":\"2024-06-30T08:45:08.676112Z\",\"iopub.status.idle\":\"2024-06-30T08:45:08.684466Z\",\"shell.execute_reply.started\":\"2024-06-30T08:45:08.676068Z\",\"shell.execute_reply\":\"2024-06-30T08:45:08.683158Z\"},\"jupyter\":{\"outputs_hidden\":false}}\nreg.predict(np.array([[3.5]]))\n\n# %% [code] {\"execution\":{\"iopub.status.busy\":\"2024-06-30T08:45:08.685865Z\",\"iopub.execute_input\":\"2024-06-30T08:45:08.686281Z\",\"iopub.status.idle\":\"2024-06-30T08:45:08.721136Z\",\"shell.execute_reply.started\":\"2024-06-30T08:45:08.686244Z\",\"shell.execute_reply\":\"2024-06-30T08:45:08.720053Z\"},\"jupyter\":{\"outputs_hidden\":false}}\nfrom sklearn.linear_model import SGDRegressor\nfrom sklearn.pipeline import make_pipeline\nfrom sklearn.preprocessing import StandardScaler\n\nreg = make_pipeline(StandardScaler(),\n                    SGDRegressor(max_iter=1000, tol=1e-3))\nreg.fit(x_train, y_train)\n\n# %% [code] {\"execution\":{\"iopub.status.busy\":\"2024-06-30T08:45:08.722530Z\",\"iopub.execute_input\":\"2024-06-30T08:45:08.722933Z\",\"iopub.status.idle\":\"2024-06-30T08:45:08.732195Z\",\"shell.execute_reply.started\":\"2024-06-30T08:45:08.722893Z\",\"shell.execute_reply\":\"2024-06-30T08:45:08.730740Z\"},\"jupyter\":{\"outputs_hidden\":false}}\nreg.score(x_train, y_train)\n\n# %% [code] {\"execution\":{\"iopub.status.busy\":\"2024-06-30T08:45:08.733893Z\",\"iopub.execute_input\":\"2024-06-30T08:45:08.734638Z\",\"iopub.status.idle\":\"2024-06-30T08:45:08.744468Z\",\"shell.execute_reply.started\":\"2024-06-30T08:45:08.734596Z\",\"shell.execute_reply\":\"2024-06-30T08:45:08.743324Z\"},\"jupyter\":{\"outputs_hidden\":false}}\nreg.predict(np.array([[3.5]]))\n\n# %% [code] {\"execution\":{\"iopub.status.busy\":\"2024-06-30T13:10:02.800614Z\",\"iopub.execute_input\":\"2024-06-30T13:10:02.801126Z\",\"iopub.status.idle\":\"2024-06-30T13:10:03.057331Z\",\"shell.execute_reply.started\":\"2024-06-30T13:10:02.801089Z\",\"shell.execute_reply\":\"2024-06-30T13:10:03.056268Z\"},\"jupyter\":{\"outputs_hidden\":false}}\ndef f_x(x_i, w, b):\n    return x_i*w + b\n\ndef compute_cost(X, y, w, b):\n    \"\"\"\n      X: The training dataset of m size and n features\n      y: The historically predicted values of y\n    \"\"\"\n    m = X.shape[0]\n    total_cost = 0\n    for i in range(m):\n        cost = (f_x(X[i][0], w, b) - y[i])**2\n        total_cost += cost\n    return total_cost / (2*m)\n\nb = 0\ncost_array = []\nW = [i for i in range(-10,11)]\ny_train_10 = np.array([x/10000 for x in y_train])  # Values scaled down by 10000 for graphing\nfor i in W:\n    cost_at_w = compute_cost(x_train, y_train_10, i, b)\n    cost_array.append(cost_at_w)\nplt.plot(W, cost_array)\nplt.title(\"Cost Function Trend wrt different values of w\")\nplt.xlabel(\"w\")\nplt.ylabel(\"J(w,b)\")\nplt.show()\n\n# %% [code] {\"execution\":{\"iopub.status.busy\":\"2024-06-30T13:30:21.442486Z\",\"iopub.execute_input\":\"2024-06-30T13:30:21.442896Z\",\"iopub.status.idle\":\"2024-06-30T13:30:21.464003Z\",\"shell.execute_reply.started\":\"2024-06-30T13:30:21.442863Z\",\"shell.execute_reply\":\"2024-06-30T13:30:21.462777Z\"},\"jupyter\":{\"outputs_hidden\":false}}\ndef compute_gradient(X, y, w, b):\n    dj_dw , dj_db = 0, 0\n    m = X.shape[0]\n    for i in range(m):\n        f_x_i = f_x(X[i][0], w, b)\n        dj_dw += (f_x_i - y[i]) * X[i][0]\n        dj_db += (f_x_i - y[i]) \n    dj_dw = dj_dw / m\n    dj_db = dj_db/ m\n    return dj_dw, dj_db\n\ndef run_gradient_descent(X, y, w, b, alpha=0.01):\n    m = X.shape[0]\n    lines = []\n    y1 = 0\n    y2 = max(y)\n    for i in range(100):\n        dj_dw , dj_db = compute_gradient(X, y, w, b)\n        w = w - alpha*dj_dw\n        b = b - alpha*dj_db\n        x1 = (y1 - b) / w\n        x2 = (y2 - b) / w\n        lines.append(([x1,x2],[y1,y2]))\n    return w,b,lines\n\ndef predict_final_value(w,b,x_pred):\n    y_pred = x_pred*w + b\n    return y_pred\n\nw,b,lines = run_gradient_descent(x_train, y_train_10,0, 0)\n\n# %% [code] {\"execution\":{\"iopub.status.busy\":\"2024-06-30T13:30:28.771395Z\",\"iopub.execute_input\":\"2024-06-30T13:30:28.771788Z\",\"iopub.status.idle\":\"2024-06-30T13:30:29.057523Z\",\"shell.execute_reply.started\":\"2024-06-30T13:30:28.771757Z\",\"shell.execute_reply\":\"2024-06-30T13:30:29.056366Z\"},\"jupyter\":{\"outputs_hidden\":false}}\n# Line Eqn = wx+b\nx_line = []\nx_line.append((y_train_10[0] - b) / w)\nx_line.append((y_train_10[-1] - b) / w)\ny_line = [y_train_10[0],y_train_10[-1]]\nplt.scatter(df[\"YearsExperience\"],y_train_10,color=\"red\")\nplt.plot(x_line, y_line,color=\"blue\")\nplt.xlabel(\"YOE in years\")\nplt.ylabel(\"Salary\")\n\n# %% [code] {\"execution\":{\"iopub.status.busy\":\"2024-06-30T13:30:42.101381Z\",\"iopub.execute_input\":\"2024-06-30T13:30:42.101799Z\",\"iopub.status.idle\":\"2024-06-30T13:30:42.110492Z\",\"shell.execute_reply.started\":\"2024-06-30T13:30:42.101768Z\",\"shell.execute_reply\":\"2024-06-30T13:30:42.108959Z\"},\"jupyter\":{\"outputs_hidden\":false}}\npredict_final_value(w,b,3.5)\n\n# %% [code] {\"execution\":{\"iopub.status.busy\":\"2024-06-30T13:32:51.457719Z\",\"iopub.execute_input\":\"2024-06-30T13:32:51.458155Z\",\"iopub.status.idle\":\"2024-06-30T13:32:59.661147Z\",\"shell.execute_reply.started\":\"2024-06-30T13:32:51.458123Z\",\"shell.execute_reply\":\"2024-06-30T13:32:59.660196Z\"},\"jupyter\":{\"outputs_hidden\":false}}\nimport matplotlib.animation as animation\nfrom IPython.display import HTML\n\nfig, ax = plt.subplots()\nax.scatter(df[\"YearsExperience\"],y_train_10,color=\"red\",marker=\"+\")\nax.set_xlim(0,10)\nax.set_ylim(0,15)\n\nline, = ax.plot([], [], color=\"blue\")\n\ndef init():\n    line.set_data([], [])\n    return line,\n\ndef update(frame):\n    xdata, ydata = lines[frame]\n    line.set_data(xdata, ydata)\n    return line,\n\nani = animation.FuncAnimation(fig, update, frames=len(lines), init_func=init, blit=True, repeat=True)\nHTML(ani.to_jshtml())\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false}}\n","metadata":{"_uuid":"698d72f6-2aba-4394-bcd5-e3379c6c387b","_cell_guid":"abe6811e-c8dd-43ed-ba2f-3b6a964b0ab3","collapsed":false,"jupyter":{"outputs_hidden":false},"trusted":true},"execution_count":null,"outputs":[]}]}