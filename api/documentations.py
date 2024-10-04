from drf_yasg import openapi

manual_parameters = [
    openapi.Parameter(
        'breed_id',
        openapi.IN_QUERY,
        description="Filter by breed ID. Pass an integer or leave empty to show all kittens.",
        type=openapi.TYPE_INTEGER,
        required=False
    )
]

manual_parameters_rating = [
    openapi.Parameter(
        'kitten_id',
        openapi.IN_QUERY,
        description="Filter by kitten ID. Pass an integer or leave empty to show all kitten ratings.",
        type=openapi.TYPE_INTEGER,
        required=False
    )
]

get_detail_response_documentation = {
    200: openapi.Response(
        description="Kitten detail",
        schema=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            title='Kitten',
            properties={
                'id': openapi.Schema(
                    type=openapi.TYPE_INTEGER,
                    description='ID of the kitten',
                    title='ID',
                    read_only=True
                ),
                'color': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description='Color of the kitten',
                    title='Color',
                    maxLength=255,
                    minLength=1,
                ),
                'age': openapi.Schema(
                    type=openapi.TYPE_INTEGER,
                    description='Age of the kitten',
                    title='Age',
                    maximum=2147483647,
                    minimum=0,
                ),
                'description': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description='Description of the kitten',
                    title='Description',
                    minLength=1,
                ),
                'user': openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    description='Owner of the kitten',
                    title='Owner',
                    properties={
                        'id': openapi.Schema(
                            type=openapi.TYPE_INTEGER,
                            description='ID of the owner',
                            title='ID',
                            read_only=True,
                        ),
                        'first_name': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='First name of the owner',
                            title='First name',
                            maxLength=255,
                            minLength=1,
                        ),
                        'last_name': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Last name of the owner',
                            title='Last name',
                            maxLength=255,
                            minLength=1,
                        ),
                        'email': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Email address of the owner',
                            title='Email',
                            maxLength=255,
                            minLength=1,
                        ),
                        'username': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Username of the owner',
                            title='Username',
                            maxLength=255,
                            minLength=1,
                        ),
                    }
                ),
                'breed': openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'id': openapi.Schema(
                            type=openapi.TYPE_INTEGER,
                            description='ID of the breed',
                            title='ID',
                            read_only=True,
                        ),
                        'name': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Name of the kitten',
                            title='Name',
                            maxLength=255,
                            minLength=1,
                        ),
                    },
                    description='Breed of the kitten'
                ),
            }
        ),
    ),
}

get_data_response_documentation = {
    200: openapi.Response(
        description="Kitten data",
        title="Kitten",
        schema=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'id': openapi.Schema(
                    type=openapi.TYPE_INTEGER,
                    description='ID of the kitten',
                    title='ID',
                    read_only=True,
                ),
                'color': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description='Color of the kitten',
                    title='Color',
                    maxLength=255,
                    minLength=1,
                ),
                'age': openapi.Schema(
                    type=openapi.TYPE_INTEGER,
                    description='Age of the kitten',
                    title='Age',
                    maximum=2147483647,
                ),
                'description': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description='Description of the kitten',
                    title='Description',
                    minLength=1,
                ),
                'user': openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    description='Owner of the kitten',
                    title='Owner',
                    properties={
                        'id': openapi.Schema(
                            type=openapi.TYPE_INTEGER,
                            description='ID of the owner',
                            title='ID',
                            read_only=True,
                        ),
                        'first_name': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='First name of the owner',
                            title='First name',
                            maxLength=255,
                            minLength=1,
                        ),
                        'last_name': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Last name of the owner',
                            title='Last name',
                            maxLength=255,
                            minLength=1,
                        ),
                        'email': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Email address of the owner',
                            title='Email',
                            maxLength=255,
                            minLength=1,
                        ),
                        'username': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Username of the owner',
                            title='Username',
                            maxLength=255,
                            minLength=1,
                        ),
                    }
                ),
                'breed': openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    title='Breed',
                    properties={
                        'id': openapi.Schema(
                            type=openapi.TYPE_INTEGER,
                            description='ID of the breed',
                            title='ID',
                            read_only=True,
                        ),
                        'name': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Name of the kitten',
                            title='Name',
                            maxLength=255,
                            minLength=1,
                        ),
                    },
                    description='Breed of the kitten'
                ),
            }
        ),
    ),
}

post_data_request_documentation = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    title='Kitten data',
    properties={
        'color': openapi.Schema(
            type=openapi.TYPE_STRING,
            description='Color of the kitten',
            title='Color',
            maxLength=255,
            minLength=1,
        ),
        'age': openapi.Schema(
            type=openapi.TYPE_INTEGER,
            description='Age of the kitten',
            title='Age',
            maximum=2147483647,
        ),
        'description': openapi.Schema(
            type=openapi.TYPE_STRING,
            description='Description of the kitten',
            title='Description',
            minLength=1,
        ),
        'breed_id': openapi.Schema(
            type=openapi.TYPE_INTEGER,
            description='ID of the breed',
            title='Breed_ID',
        ),
    },
    required=['color', 'age', 'description', 'breed_id']
)

put_data_request_documentation = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'breed_id': openapi.Schema(
            type=openapi.TYPE_INTEGER,
            description='ID of the breed',
            title='Breed_ID',
        ),
        'color': openapi.Schema(
            type=openapi.TYPE_STRING,
            description='Color of the kitten',
            title='Color',
            maxLength=255,
            minLength=1,
        ),
        'age': openapi.Schema(
            type=openapi.TYPE_INTEGER,
            description='Age of the kitten',
            title='Age',
            maximum=2147483647,
        ),
        'description': openapi.Schema(
            type=openapi.TYPE_STRING,
            description='Description of the kitten',
            title='Description',
            minLength=1,
        ),
    },
    required=['breed_id'],
)

patch_data_request_documentation = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    title='Kitten data',
    properties={
        'breed_id': openapi.Schema(
            type=openapi.TYPE_INTEGER,
            description='ID of the breed',
            title='Breed_ID',
        ),
        'color': openapi.Schema(
            type=openapi.TYPE_STRING,
            description='Color of the kitten',
            title='Color',
            maxLength=255,
            minLength=1,
        ),
        'age': openapi.Schema(
            type=openapi.TYPE_INTEGER,
            description='Age of the kitten',
            title='Age',
            maximum=2147483647,
        ),
        'description': openapi.Schema(
            type=openapi.TYPE_STRING,
            description='Description of the kitten',
            title='Description',
            minLength=1,
        ),
    },
)

post_data_response_documentation = {
    201: openapi.Response(
        description="Add kitten data",
        schema=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'id': openapi.Schema(
                    type=openapi.TYPE_INTEGER,
                    description='ID of the kitten',
                    title='ID',
                ),
                'color': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description='Color of the kitten',
                    title='Color',
                    maxLength=255,
                    minLength=1,
                ),
                'age': openapi.Schema(
                    type=openapi.TYPE_INTEGER,
                    description='Age of the kitten',
                    title='Age',
                    maximum=2147483647,
                ),
                'description': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description='Description of the kitten',
                    title='Description',
                    minLength=1,
                ),
                'breed': openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    title='Breed',
                    properties={
                        'id': openapi.Schema(
                            type=openapi.TYPE_INTEGER,
                            description='ID of the breed',
                            title='ID',
                            read_only=True,
                        ),
                        'name': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Name of the kitten',
                            title='Name',
                            minLength=1,
                            maxLength=255,
                        ),
                    },
                    description='Breed of the kitten'
                ),
            }
        ),
    ),
}

rating_request_documentation = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'kitten': openapi.Schema(
            type=openapi.TYPE_OBJECT,
            description='ID of the kitten being rated.',
            title='Kitten',
            properties={
                'id': openapi.Schema(
                    type=openapi.TYPE_INTEGER,
                    description='ID of the kitten',
                    title='ID',
                    read_only=True
                ),
                'color': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description='Color of the kitten',
                    title='Color',
                    maxLength=255,
                    minLength=1,
                ),
                'age': openapi.Schema(
                    type=openapi.TYPE_INTEGER,
                    description='Age of the kitten',
                    title='Age',
                    maximum=2147483647,
                    minimum=0,
                ),
                'description': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description='Description of the kitten',
                    title='Description',
                    minLength=1,
                ),
                'user': openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    description='Owner of the kitten',
                    title='Owner',
                    properties={
                        'id': openapi.Schema(
                            type=openapi.TYPE_INTEGER,
                            description='ID of the owner',
                            title='ID',
                            read_only=True,
                        ),
                        'first_name': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='First name of the owner',
                            title='First name',
                            maxLength=255,
                            minLength=1,
                        ),
                        'last_name': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Last name of the owner',
                            title='Last name',
                            maxLength=255,
                            minLength=1,
                        ),
                        'email': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Email address of the owner',
                            title='Email',
                            maxLength=255,
                            minLength=1,
                        ),
                        'username': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Username of the owner',
                            title='Username',
                            maxLength=255,
                            minLength=1,
                        ),
                    }
                ),
            }
        ),
        'user': openapi.Schema(
            type=openapi.TYPE_OBJECT,
            description='ID of the user being rated.',
            title='User',
            properties={
                'id': openapi.Schema(
                    type=openapi.TYPE_INTEGER,
                    description='ID of the owner',
                    title='ID',
                    read_only=True,
                ),
                'first_name': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description='First name of the owner',
                    title='First name',
                    maxLength=255,
                    minLength=1,
                ),
                'last_name': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description='Last name of the owner',
                    title='Last name',
                    maxLength=255,
                    minLength=1,
                ),
                'email': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description='Email address of the owner',
                    title='Email',
                    maxLength=255,
                    minLength=1,
                ),
                'username': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description='Username of the owner',
                    title='Username',
                    maxLength=255,
                    minLength=1,
                ),
            }
        ),
        'score': openapi.Schema(
            type=openapi.TYPE_INTEGER,
            description='Score given to the kitten (1 to 5).'
        ),
    },
    required=['kitten', 'score']
)
