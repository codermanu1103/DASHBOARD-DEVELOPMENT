import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import seaborn as sns

# Load dataset
df = sns.load_dataset('titanic')
df.dropna(subset=['age', 'embarked', 'sex', 'pclass', 'survived'], inplace=True)

# Initialize app
app = dash.Dash(__name__)
app.title = "Titanic Survival Dashboard"

# App Layout
app.layout = html.Div([
    html.H1("🚢 Titanic Survival Dashboard", style={'textAlign': 'center'}),

    html.Div([
        html.Label("Filter by Embarked:"),
        dcc.Dropdown(
            id='embarked-filter',
            options=[{'label': port, 'value': port} for port in df['embarked'].unique()],
            value='S',
            clearable=False
        ),
    ], style={'width': '25%', 'display': 'inline-block'}),

    html.Div([
        dcc.Graph(id='survival-bar')
    ]),

    html.Div([
        dcc.Graph(id='age-histogram')
    ])
])

# Callbacks
@app.callback(
    [Output('survival-bar', 'figure'),
     Output('age-histogram', 'figure')],
    [Input('embarked-filter', 'value')]
)
def update_graphs(selected_port):
    filtered_df = df[df['embarked'] == selected_port]

    fig1 = px.bar(
        filtered_df.groupby('sex')['survived'].mean().reset_index(),
        x='sex', y='survived',
        labels={'survived': 'Survival Rate'},
        title=f"Survival Rate by Sex (Embarked: {selected_port})"
    )

    fig2 = px.histogram(
        filtered_df,
        x='age',
        nbins=20,
        color='survived',
        labels={'survived': 'Survived'},
        title=f"Age Distribution (Embarked: {selected_port})"
    )

    return fig1, fig2

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
