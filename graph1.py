# Use the plotly library using a shorthand 'px' to refer to it
import plotly.express as px

# Load the data from Gapminder and into a variable called df
# (short for data frame) that plotly can use.
df = px.data.gapminder()

# Create the bubble chart
fig = px.scatter(df.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent", hover_name="country", log_x=True, size_max=60)

# Display the chart
fig.show()
