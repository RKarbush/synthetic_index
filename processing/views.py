# Django imports
from django.http.response import HttpResponse, JsonResponse
# Personal/local imports
from gathering.views import gather_data
from .models import uploadfolder
# Others
import pandas as pd
import json


def security_return_by_date(Pit, Pit_1):
    """
        Function that returns the security's ith return on its correspondant date t (rit).
        parameters: 
            Pit - current underlying security's price
            Pit_1 - previous underlying security's price
    """

    return (Pit/Pit_1) - 1


def index_return_by_date(price_t_1, price_t, weights):
    """ 
        Function that returns the calculated return of an index on date t (Rt) 
        parameters:
            price_t_1 - pandas' series of underlying security's t price
            price_t - pandas' series of underlying security's t-1 price
            weights - pandas' series of weights
    """
    Rt = 0
    for i, p in price_t.iteritems():
        Rt += weights[i] * security_return_by_date(price_t_1[i], p)

    return Rt


def synthetic_index(dataframe):
    """ 
        Function that returns an array indexed by date t of synthetic index (Applies the synthetic index formula Pt).
        parameters:
            dataframe - gathered data from a file such as Excel, prepared to be processed.
    """
    Pt_array = [] # Synthetic Index (Pt) array indexed by t
    weights = dataframe.iloc[0]
    Pt_1 = 100 # P sub0
    Pt_array.append(Pt_1) 
    prices = dataframe.loc[1:, dataframe.columns != 'Id'] # A dataframe with only the rows correspondant to prices
    for t, price_t in prices[1:].iterrows(): # The [1:] is necessary because we already have P sub0
        price_t_1 = prices.loc[t-1]
        Rt = index_return_by_date(price_t_1, price_t, weights)
        Pt = Pt_1 * (1 + Rt)
        Pt_1 = Pt
        Pt_array.append(round(Pt, 2))

    return Pt_array


def synthetic_index_example(filename):
    """
        Function that returns a synthetic index array of a given data file, only if this file exists. The result is also
        stored on the database, specifically as a field of the corresponding object.
        parameters:
            filename - name of the file containing the data.
    """
    dataframe = gather_data(filename)
    if type(dataframe) is pd.core.frame.DataFrame:
        Pt_array = synthetic_index(dataframe)
        # try:
        data_folder = uploadfolder.objects.get(File_to_upload=filename)
        # except uploadfolder.MultipleObjectsReturned:


        data_folder.synth_index_array = json.dumps(Pt_array)
        data_folder.save()
        return Pt_array
    else: # return the error message
        return dataframe


def synthetic_index_web_example(request):
    """
        Function that returns the result as an array indexed by date t of synthetic index and a csv to download. 
        parameters:
            request - needed to check what type of method is being requested to answer correspondingly
    """
    if request.method=="GET":
        Pt_array = synthetic_index_example("Data.xlsx")

        pd.DataFrame(Pt_array).to_csv("static/synthetic_index/export/synthIndex.csv")

        context = {
            "result": Pt_array
        }
        return JsonResponse(context, status=200)