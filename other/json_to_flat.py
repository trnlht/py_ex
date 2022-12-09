import unittest


"""
Необходимо преобразовать json к плоскому виду, например:

{
    "service_version": "2022.08.02",
    "logs_store": {
        "remote": {
            "url": "https://elk",
            "user": "some_user",
            "password": "some_password"
        },
        "local": "$HOME/service.log"
    },
    "message_broker":
    {
        "url": "https://rabbitmq",
        "user": "rmq",
        "password": "some_password"
    }
}

=>

{
    "service_version": "2022.08.02",
    "logs_store.remote.url": "https://elk",
    "logs_store.remote.user": "some_user",
    "logs_store.remote.password": "some_password",
    "logs_store.local": "$HOME/service.log",
    "message_broker.url": "https://rabbitmq",
    "message_broker.user": "rmq",
    "message_broker.password": "some_password"
}

"""


def json_to_flat(input_json, output_json, prefix=""):
    for k, v in input_json.items():
        if prefix:
            k = ".".join((prefix, k))

        if not isinstance(v, dict):
            output_json[k] = v
        else:
            json_to_flat(input_json=v, output_json=output_json, prefix=k)


class JsonToFlatTester(unittest.TestCase):

    def test_should_correct_transform_simple_json(self):
        input_json = {"a": 1, "b": 2, "c": 3}
        output_json = {}
        json_to_flat(input_json=input_json, output_json=output_json)

        self.assertEqual(input_json, output_json)

    def test_should_correct_transform_json_with_double_nesting(self):
        input_json = {"a": 1, "b": {"a": 1, "b": 2, "c": 3}, "c": 3}
        output_json = {}
        json_to_flat(input_json=input_json, output_json=output_json)

        self.assertEqual(output_json, {"a": 1, "b.a": 1, "b.b": 2, "b.c": 3, "c": 3})

    def test_should_correct_transform_json_with_triple_nesting(self):
        input_json = {"a": 1,
                      "b":
                          {"a": 1,
                           "b":
                               {"a": 1,
                                "b": 2,
                                "c": 3},
                           "c": 3},
                      "c": 3}
        output_json = {}
        json_to_flat(input_json=input_json, output_json=output_json)

        self.assertEqual(output_json, {"a": 1, "b.a": 1, "b.b.a": 1, "b.b.b": 2, "b.b.c": 3, "b.c": 3, "c": 3})

    def test_should_correct_transform_json_with_real_example(self):
        input_json = {
            "service_version": "2022.08.02",
            "logs_store": {
                "remote": {
                    "url": "https://elk",
                    "user": "some_user",
                    "password": "some_password"
                },
                "local": "$HOME/service.log"
            },
            "message_broker":
                {
                    "url": "https://rabbitmq",
                    "user": "rmq",
                    "password": "some_password"
                }
        }

        output_json = {}

        expected_json = {
            "service_version": "2022.08.02",
            "logs_store.remote.url": "https://elk",
            "logs_store.remote.user": "some_user",
            "logs_store.remote.password": "some_password",
            "logs_store.local": "$HOME/service.log",
            "message_broker.url": "https://rabbitmq",
            "message_broker.user": "rmq",
            "message_broker.password": "some_password"
        }

        json_to_flat(input_json=input_json, output_json=output_json)

        self.assertEqual(output_json, expected_json)


if __name__ == "__main__":
    unittest.main(verbosity=2)
