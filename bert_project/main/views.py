from django.shortcuts import render
from django.utils import timezone # settings.py의 timezone을 따라감
from django.conf import settings

import pandas as pd
from . import inference_bert
from . import bert_load

def index(request):
    current_time = timezone.now()
    context = {'current_time':current_time}
    return render(request, 'main/index.html', context)


def bert_input(request):
    reviews_df = pd.read_table('./data/naver_shopping.txt', names=['ratings', 'reviews'])
    reviews_df = reviews_df.drop_duplicates('reviews')
    reviews_df = reviews_df.reset_index(drop=True)
    reviews_df['label'] = reviews_df['ratings'].apply(lambda x : 1 if x > 3 else 0) # ratings에 따라 0 or 1을 가지는 label 열 생성
    reviews_df = reviews_df.head()

    reviews_df_html = reviews_df.to_html(
                            columns=['reviews', 'label'],
                            index=False, na_rep="", bold_rows=True,
                            classes=["table", "table-hover", "table-processed"])

    context = {'reviews_df_html':reviews_df_html}
    return render(request, 'main/bert_input.html', context)


def bert_predict(request):
    target_sentence = request.POST['target_sentence']

    tokenizer = settings.TOKENIZER_KOBERT
    model = settings.MODEL_KOBERT

    result_bert = inference_bert.predict_sentiment(target_sentence, tokenizer, model)

    context = {'target_sentence':target_sentence,
               'result_bert':result_bert}
    return render(request, 'main/bert_predict.html', context)
