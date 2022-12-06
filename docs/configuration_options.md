# Configuration options

This page lists configuration option specific to MESOC Toolkit API. For additional configuration options not shown here, see documentation of specific dependency listed below:

- [Django Web Framework](https://docs.djangoproject.com/en/3.1/ref/settings/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Django CORS headers](https://github.com/adamchainz/django-cors-headers)
- [Celery Task Queue](https://docs.celeryq.dev/en/v5.0.2/index.html)
- [uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/)
- [Anymail](https://anymail.dev/en/v8.2/)


```{note}
All URLs are specified without trailing slash, e.g. `https://localhost:8000`.
```

`CORE_FEEDBACK_EMAL`  

Email to send feedback to.

`CORE_API_BASE_URL`

Base API URL.


`CORE_PASSWORD_RESET_BASE_URL`

Link to password reset page sent to the user by email. The API will add UUID path parameter to the URL which identifies password reset request.

`CORE_PASSWORD_RESET_MAX_AGE`

Time in days before password reset request expires.

`CORE_VERIFICATION_BASE_URL`

Link to account verification page sent to the user by email. The API will add UUID path parameter to the URL which identifies generated verification request.

`CORE_VERIFICATION_MAX_AGE`

Time in days before verification request expires.

`CORE_PROCESSING_SUCCESS_URL`

Link to page displaying successfully processed document sent to the user by email.

`CORE_PROCESSING_FAIL_URL`

Link to page displaying unsuccessfully processed document sent to the user by email.

`CORE_FILE_MAX_SIZE`

Maximum file upload size in bytes. Default is 30 MiB.

```{important}
Make sure HTTP server is configured to allow sufficiently large payload size to accommodate for increased file upload size, e.g. `client_max_body_size` in Nginx.
```

`CORE_ALLOWED_MIME_TYPES`

Allowed MIME types on upload. Default are `application/pdf` and `text/plain`.

`CORE_ALLOWED_EXTENSIONS`

Allowed file extensions on upload. Default are `pdf` and `txt`.

`CORE_YAKE_CANDIDATE_NGRAM`

N-grams to consider when extracting keywords with YAKE, value of 3 will consider phrases of up to 3 words. Default is 4.


`CORE_YAKE_CANDIDATE_WINDOW_SIZE`

The size of sliding window in words used for computing co-occurrence count. Co-occurrence is used in YAKE to filter out irrelevant words. Default is 18.


`CORE_YAKE_THRESHOLD`

Similarity threshold for candidate keywords. Candidate keywords exceeding this threshold will be discarded in order to filter out duplicate keywords. Default is 0.95.


`CORE_CRP_ROW_MODEL`

Path to CRP row classification model. Default is `BASE_DIR / 'ml_models' / 'rf_row.pickle'`.

`CORE_CRP_COLUMN_MODEL`

Path to CRP column classification model. Default is `BASE_DIR / 'ml_models' / 'rf_column.pickle'.`

`CORE_CRP_TFIDF_VECTORIZER`
 
Path to CRP TF-IDF vectorizer model. Default is ```BASE_DIR / 'ml_models' / 'tfidf_vectorizer.pickle'.```

`CORE_CRP_COLUMN_THRESHOLD`

Classification threshold for CRP column classifier. Columns below this threshold will be discarded and it's probabilities uniformly redistributed to other columns.

`CORE_CRP_ROW_THRESHOLD`

Classification threshold for CRP row classifier. Rows below this threshold will be discarded and it's probabilities uniformly redistributed to other rows.

`CORE_NUM_KEYWORDS`

Maximum number of keywords to extract from uploaded documents. Default is 30.

`CORE_MIN_SENTENCE_LENGTH`

Minimum number of characters in a sentence for it to be processed. Default is 15.

`CORE_NUM_SIMILAR_DOCUMENTS`

Number of returned similar documents. Default is 10.

`CORE_CELL_SIMILARITY_THRESHOLD`

Document similarity threshold by cell. Documents below this threshold will not be returned. Default is 0.3.

`CORE_IMPACT_SIMILARITY_THRESHOLD`

Document similarity threshold by impact. Documents below this threshold will not be returned. Default is 0.005.

`CORE_REPOSITORY_PREVIEW_URL`

Base repository URL for previewing similar documents. The API will append 
`/<id>.html` when returning URL for every retrieved repository document.

`CORE_GOOGLE_CLOUD_CREDENTIALS`

Google Cloud Credentials JSON specified as a Python dictionary.

`CORE_GOOGLE_GEO_API_KEY`

Google GeoAPI key.