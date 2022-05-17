from unittest.mock import MagicMock, Mock, patch

import requests_mock

from rocksteady import think


class Tester(object):
    @patch("rocksteady.think.check_output")
    def test_print_contents_of_cwd(self, mock_check_output):
        mock_check_output.return_value = b"cobra\nkai"
        actual_result = think.print_contents_of_cwd()

        expected_directory = b"cobra"
        assert expected_directory in actual_result

    @requests_mock.Mocker(kw="http_mocker")
    def test_get_google(self, **kwargs):
        kwargs["http_mocker"].get(
            "https://www.google.com/", json={"name": "awesome-mock"}
        )
        resp = think.get_google()

        assert resp == {"name": "awesome-mock"}

    @patch("rocksteady.think.requests")
    def test_get_google2(self, mock_requests):
        mock_requests.get.return_value = Mock(
            **{"json.return_value": {"name": "awesome-mock"}}
        )
        resp = think.get_google()

        assert resp == {"name": "awesome-mock"}

    @patch("rocksteady.think.requests")
    def test_get_google3(self, mock_requests):
        mock_requests.get.return_value = MagicMock(
            **{"json.return_value": {"name": "awesome-mock"}}
        )
        resp = think.get_google()

        assert resp == {"name": "awesome-mock"}

    @patch("rocksteady.think.Wrench")
    def test_wrench(self, mock_wrench):
        mock_wrench.return_value = MagicMock(wrencher=MagicMock(return_value=15))
        resp = think.wrench_out()

        mock_wrench.assert_called_once()
        assert resp == 15

    @patch("rocksteady.think.Wrench")
    @patch("rocksteady.think.check_output")
    def test_wrench_and_check_output(self, mock_check_output, mock_wrench):
        mock_wrench.return_value = MagicMock(wrencher=MagicMock(return_value=15))
        resp = think.wrench_out()

        mock_wrench.assert_called_once()
        assert resp == 15

        mock_check_output.return_value = b"cobra\nkai"
        actual_result = think.print_contents_of_cwd()

        expected_directory = b"cobra"
        assert expected_directory in actual_result

    @patch("rocksteady.think.Wrench")
    def test_wrench_side_effect(self, mock_wrench):
        mock_wrench.return_value = MagicMock(
            wrencher=MagicMock(side_effect=[15, 20, 25])
        )
        assert think.wrench_out() == 15
        assert think.wrench_out() == 20
        assert think.wrench_out() == 25
        assert mock_wrench.call_count == 3

    @patch("rocksteady.think.Wrench")
    def test_wrench_side_effect_exc(self, mock_wrench):
        mock_wrench.return_value = MagicMock(
            wrencher=MagicMock(side_effect=[15, 20, ZeroDivisionError()])
        )
        assert think.wrench_out() == 15
        assert think.wrench_out() == 20
        try:
            think.wrench_out()
        except ZeroDivisionError as e:
            assert not e.__str__()
        assert mock_wrench.call_count == 3
