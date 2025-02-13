import plotly.graph_objects as go
potential = [ 4,  9,  3,  5,  4]
companies = ['Stark Ind.', 'Wayne Ent.', 'Lexcorp', 'Oscorp', 'ACME']
valuation = [41, 37, 31, 26, 24]
fig = go.Figure([
    go.Bar(orientation='h', y=companies, x=valuation, name='Worth'),
    go.Bar(orientation='h', y=companies, x=potential, name='Growth')
])

fig.update_layout(barmode='stack')
fig.show()