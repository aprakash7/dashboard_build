import pandas as pd
import dash
import dash_core_components as dcc
import plotly
import plotly.express as px
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import pathlib
import dash_html_components as html
import dash_table


import chart_studio
import chart_studio.plotly as py
import chart_studio.tools as tls

#import io
#from base64 import b64encode
#buffer = io.StringIO()

#api= 'T2IQHbtqC9s6vztmxR9K'
#username= 'aprakash7'
#chart_studio.tools.set_credentials_file(username= username, api_key= api)


#note that the graph is actually Rk = slope* interecpt + c
df= pd.read_csv(r'C:\Users\Akshay Prakash\Downloads\1995_96 - 2020 Premier league standings.csv')

mark_values= {1996:'1996', 1997: '1997', 1998: '1998', 1999: '1999',
              2000: '2000', 2001: '2001', 2002: '2002', 2003: '2003',
              2004: '2004', 2005: '2005', 2006: '2006', 2007: '2007',
              2008: '2008', 2009: '2009', 2010: '2010', 2011: '2011',
              2012: '2012', 2013: '2013', 2014: '2014', 2015: '2015',
              2016: '2016', 2017: '2017', 2018: '2018', 2019: '2019',
              2020: '2020'  }

Rk_values= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

dff_vis= df[df['Rk'].isin(Rk_values)]
#dff_vis=
#Only 1 to 20 and then go by years
fig= px.scatter(dff_vis,
    x= "Pts",
    y= "Rk", range_y= [21, 0],
    color= 'Rk',
    animation_frame='Year', animation_group= 'Rk', range_x= [10,100], height= 800,
    hover_name= "Squad",
    hover_data= ["Top Team Scorer", "Goalkeeper", "Year"],
    title= "Data Visualisation of the entire Premier League Points history")
#fig= fig.update_traces(mode= 'markers+lines')
fig= fig.update_yaxes(autorange= "reversed", title_text= "League Position", tickvals= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
fig= fig.update_xaxes(title_text= "Points")
fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration']= 1000
fig.layout.updatemenus[0].buttons[0].args[1]['transition']['duration']= 100
#fig.write_html(buffer)

#html_bytes = buffer.getvalue().encode()
#encoded = b64encode(html_bytes).decode()
#py.plot(fig,filename= ' Premier league Points history', auto_open= True)


app = dash.Dash(__name__, prevent_initial_callbacks=True, meta_tags= [{'name': 'viewport', 'content': 'width= device-width'}])

app.layout = html.Div([
                        html.Div([
                            html.Div([
                                html.H2("English Premier League", style= {"text-align": "center"}),
                                    html.Div([
                                        html.A(
                                            html.Button(
                                        "Source",
                                        style= { 'background': '#C9F1F3',
"border": "None",
                                        "position": "absolute",
                                        "top": "14px",
                                        "right": "40px",
                                        "cursor": "pointer",
                                        "font-size": "16px",
                                        "padding": "10px 32px"}
                                            ), href=  "https://fbref.com/en/comps/9/Premier-League-Stats"
                                             )
                                             ])
                                     ])

                                     ], style = {"background": "white"}),
                    html.Div([
                        html.Div([
                            dcc.Graph(id= "the_graph")
                        ]),
                        html.Div([
                            html.Div([
                                    html.H3(
                                        id= 'The_mean'
                                    ),
                                    html.P(
                                    "Mean"
                                    )
                            ], style= {
"border-radius": "5px", "background-color": "#f9f9f9", "margin": "10px",  "padding": "15px", "position": "relative",
"box-shadow": "2px 2px 2px lightgrey", "text-align": "center", "width": "194px"

                            }),
                            html.Div([
                                html.H3(
                                id= "total_points"
                                ),
                                html.P(
                                "Total Points"
                                )
                            ], style= {
"border-radius": "5px", "background-color": "#f9f9f9", "margin": "10px",  "padding": "15px", "position": "relative",
"box-shadow": "2px 2px 2px lightgrey", "text-align": "center", "width": "194px"

                            }),
                            html.Div([
                                html.H3(
                                id= 'no_of_years_in_range'
                                ),
                                html.P(
                                "Number of season(s) in range"
                                )
                            ], style= {
"border-radius": "5px", "background-color": "#f9f9f9", "margin": "10px",  "padding": "15px", "position": "relative",
"box-shadow": "2px 2px 2px lightgrey", "text-align": "center", "width": "194px"
                                })
                        ], style= {
                        "display": "flex column", "border-radius": "5px", "background-color": "#f9f9f9", "margin": "10px",  "padding": "15px", "position": "relative",
                        "box-shadow": "2px 2px 2px lightgrey", "text-align": "center", "width": "254px"

                        }),
                            html.Div([
                                html.Label("Select a Year to see actual Points table"),
                                html.Br(),
                                dcc.Dropdown(
                                id= 'checklist',
                                options= [
{'label':'1997', 'value':1997}, {'label':'1998', 'value':1998}, {'label':'1999', 'value':1999},
{'label':'2000', 'value':2000}, {'label':'2001', 'value':2001}, {'label':'2002', 'value':2002},
{'label':'2003', 'value':2003}, {'label':'2004', 'value':2005}, {'label':'2006', 'value':2006},
{'label':'2006', 'value':2006}, {'label':'2007', 'value':2007}, {'label':'2008', 'value':2008},
{'label':'2009', 'value':2009}, {'label':'2010', 'value':2010}, {'label':'2011', 'value':2011},
{'label':'2012', 'value':2012}, {'label':'2013', 'value':2013}, {'label':'2014', 'value':2014},
{'label':'2015', 'value':2015}, {'label':'2016', 'value':2016}, {'label':'2017', 'value':2017},
{'label':'2018', 'value':2018}, {'label':'2019', 'value':2019},{'label':'2020', 'value':2020},

                                ], multi= False,
                                value= '2020'
                                ),
                                dash_table.DataTable(
                                id = 'the_data_table',
                                style_cell=dict(textAlign='left'),
                                style_header=dict(backgroundColor="lightgrey"),
                                style_data=dict(backgroundColor="white")
                                ),
                            ], style= {"border-radius": "5px", "background-color": "#f9f9f9",
"margin": "10px",  "padding": "15px", "position": "relative","box-shadow": "2px 2px 2px lightgrey",
"text-align": "center", "width": "326px"}
                            )
                        ], style= {"display": "flex"}),
            html.Div([
                html.Label("Choose the range in year(s): "),
                html.P(),
                dcc.RangeSlider(id= 'the_range_slider',
                min= 1996,
                max= 2020,
                value= [1996, 2020],
                marks= mark_values,
                step= None)

            ], "display: flex"),
        html.Div([
            dcc.Graph(id='the_animated_graph')
        ]),
        html.Div([
            html.A(
            html.Button("DOWNLOAD"),
            id= 'download',
             href="data:text/html;base64," + encoded,
             download="plotly_graph.html"
             ),
            dcc.Graph(figure= fig),

        ])
])


@app.callback(
    Output('the_graph', 'figure'),
    [
    Input('the_range_slider', 'value')
    ]
)

def update_graph(years_chosen):
    #print(years_chosen)
    dff= df[(df['Year']>= years_chosen[0])&(df['Year']<= years_chosen[1])]
    # dont accept before 1996 and after 2020
    #print(dff)

    scatterplot= px.scatter(
    data_frame= dff,
    x= "Pts", width= 800,
    y= "Rk",  range_y= [21,0], height= 650,
    color= "Pts",
    trendline= 'ols', # Linear RegressionLine
    title= "Premier League Regression based on Points over seasons",
    hover_name= "Squad",
    hover_data= ["Top Team Scorer", "Goalkeeper", "Year"],
    trendline_color_override='darkblue',
    )
    scatterplot.update_traces(textposition= "top center")
    scatterplot.update_layout(hoverlabel= dict(bgcolor= "white"))
    scatterplot.update_yaxes(
    title_text= 'League Position', autorange="reversed",
    tickvals=[1, 2, 3, 4, 5, 6, 7, 8 , 9 , 10,11, 12, 13, 14, 15, 16, 17, 18, 19, 20] )

    scatterplot.update_xaxes(title_text= 'Points',
    tickvals=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
    range= [5,105])

    return scatterplot

@app.callback(
    Output('The_mean', 'children'),
    [
        Input('the_range_slider', 'value')
    ]
)
def update_mean(years_chosen): #Mean
    #print(years_chosen)
    dff= df[(df['Year']>= years_chosen[0])&(df['Year']<= years_chosen[1])]

    result= round(dff['Pts'].mean(), 2)
    #print result
    return f'{result:,}'

@app.callback(
    Output('total_points', 'children'),
    [
        Input('the_range_slider', 'value')
    ]
)

def update_total(years_chosen): #Total sum
    dff= df[(df['Year']>= years_chosen[0])&(df['Year']<= years_chosen[1])]

    result= round(dff['Pts'].sum(), 2)
    return f'{result:,}'

#Number of seasons
@app.callback(
    Output('no_of_years_in_range', 'children'),
    [
        Input('the_range_slider', 'value')
    ]
)
def update_no_of_years(years_chosen):
    dff= df[(df['Year']>= years_chosen[0])&(df['Year']<= years_chosen[1])]
    n= len(dff['Year'])
    n= int(n/20)
    #get the length of the dataframe and divide it by 20
    #print(n)
    #n= dff['Year'].nunique()
    return f'{n:,}'


#Data Frame
@app.callback([
    Output('the_data_table', 'data'),
    Output('the_data_table', 'columns'),],
    [
        Input('checklist', 'value')
    ]
)
def update_checklist(year_chosen):
    #rint(year_chosen)
    dff= df[(df['Year']== year_chosen)]
    dff= dff.rename(columns= {"Rk": "Rank"})
    dff= dff.rename(columns= {"Squad": "Team"})
    dff= dff.rename(columns= {"Pts":"Points"})
    dff= dff[['Rank', 'Team', 'Points']]
    #print(dff)
    data = dff.to_dict('rows')
    columns =  [{"name": i, "id": i,} for i in (dff.columns)]

    return data, columns

#Top 6 animated
@app.callback(
    Output('the_animated_graph', 'figure'),
    [
        Input('the_range_slider', 'value')
    ]
)
def update_animated(years_chosen):
    dff= df[(df['Year']>= years_chosen[0]) & (df['Year']<= years_chosen[1])]
    #Range slider

    Top= ['Manchester Utd', 'Manchester City', 'Tottenham', 'Chelsea', 'Arsenal', 'Liverpool']
    #Man U man city tottenham Chelsea Arsenallivepool
    dff= dff[dff['Squad'].isin(Top)]
    #Selected teams in Column Squad

    fig1= px.scatter(dff,
    x= "Pts",
    y= "Rk", range_y= [21, 0],
    text= "Squad",
    color= 'Squad', hover_name= "Squad",
    hover_data= ["Top Team Scorer", "Goalkeeper"],
    animation_frame='Year', animation_group= 'Squad', range_x= [10,100], height= 500,
    title= "Premier League Top 6 over the chosen seasons")

    fig1.update_yaxes(autorange= "reversed", title_text= "League Position")
    fig1.update_xaxes(title_text= "Points")
    fig1.update_layout(hovermode= "y unified",)
    fig1.layout.updatemenus[0].buttons[0].args[1]['frame']['duration']= 2000
    fig1.layout.updatemenus[0].buttons[0].args[1]['transition']['duration']= 300

    fig1.update_traces(marker=dict(size=10), textposition= "bottom center")

    return fig1

#py.plot(data ,filename= 'EPL Top 6 Visualisation', auto_open= True)


if __name__== "__main__":
    app.run_server(debug= True)
