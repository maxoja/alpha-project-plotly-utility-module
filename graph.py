from plotly.graph_objs import Scatter
from plotly.graph_objs import Candlestick
from plotly.graph_objs import Scatter3d
import numpy as np

def list_interval(begin, end):
    return [begin, end]

def float_list(data_list):
    return [float(x) for x in data_list]
    
def float_nparray(data_list):
    return np.array(float_list(data_list))

def flattened_list(structured_list):
    result = []
    
    for index in range(len(structured_list)):
        element = structured_list[index]
        
        if type(element) == list:
            result += flattened_list(element)
        else:
            result.append(element)
            
    return  result

def dict_without_keys(dictionary, *key_tuple):
    for k in key_tuple:
        if k in dictionary:
            dictionary.pop(k)
            
    return dictionary

def figure(layout, *obj_tuple):
    return dict(data=flattened_list(obj_tuple), layout=layout)

def slider_layout(title, x_title, y_title):
    return dict(
        title = title,
        xaxis = dict(title=x_title, rangeslider=dict()),
        yaxis = dict(title=y_title)
    )

def layout(slider=False, title='temp title', x_title='', y_title=''):
    if slider:
        return slider_layout(title, x_title, y_title)
    else:
        return dict(
            title = title,
            xaxis = dict(title=x_title),
            yaxis = dict(title=y_title)
        )
        
    
def dots_3d(x, y, z, **attributes):
    return Scatter3d(
        x = x,
        y = y,
        z = z,
        mode = 'markers',
        name = attributes['name'] if 'name' in attributes else 'unnamed-dots',
        marker = dict_without_keys(attributes, 'name')
    )

def dots_2d(x, y, **attributes):
    return Scatter(
        x = x,
        y = y,
        mode = 'markers',
        name = attributes['name'] if 'name' in attributes else 'unnamed-dots',
        marker = dict_without_keys(attributes, 'name')
    )

def candlestick(data_frame, col_open='Op', col_close='Close', col_high='High', col_low='Low'):
    return Candlestick(
        open = data_frame[col_open],
        close = data_frame[col_close],
        high = data_frame[col_high],
        low = data_frame[col_low]
    )

def trace_line_with_domain(y, x, **attributes):
    return Scatter(
        y = y,
        x = x,
        mode = 'line',
        name = attributes['name'] if 'name' in attributes else 'unnamed-line',
        line = dict_without_keys(attributes, 'name')
    )

def trace_line(y, **attributes):
    return Scatter(
        y = y,
        mode = 'line',
        name = attributes['name'] if 'name' in attributes else 'unnamed-line',
        line = dict_without_keys(attributes, 'name')
    )   

def vertical_line(x, y_begin, y_end, **attributes):
    return Scatter(
        x = list_interval(x, x),
        y = list_interval(y_begin, y_end),
        mode = 'line',
        name = attributes['name'] if 'name' in attributes else 'unnamed-line',
        line = dict_without_keys(attributes, 'name')
    )

def horizontal_line(y, x_begin, x_end, **attributes):
    return Scatter(
        x = list_interval(x_begin, x_end),
        y = list_interval(y, y),
        mode = 'line',
        name = attributes['name'] if 'name' in attributes else 'unnamed-line',
        line = dict_without_keys(attributes, 'name')
    )

if __name__ == '__main__':
    vertical_line(10,0,100)
    
