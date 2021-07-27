import plotly.graph_objects as go

fig = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 200,
      thickness = 20,
      line = dict(color = "black", width = 0.5),
      label = [1,2,3,4,5,6],
      color = "blue"
    ),
    link = dict(
      source = [0,1,2,3,3],
      target = [3,3,3,4,5],
      value = [3,3,3, 4.5,4.5]
  ))])

fig.update_layout(title_text="Basic Sankey Diagram", font_size=20)
fig.show()