import pytest
from library.package_sorter import PackageSorter
from mock import Mock, patch

class TestPackageSorter:

	@patch.object(PackageSorter, '_isBulky')
	@patch.object(PackageSorter, '_isHeavy')
	@pytest.mark.parametrize("is_bulky_return, is_heavy_return, expected",
		[
			(True, True, "REJECTED"),
			(True, False, "SPECIAL"),
			(False, True, "SPECIAL"),
			(False, False, "STANDARD")
		]
	)
	def test_sort(
		self,
		is_heavy: Mock,
		is_bulky: Mock,
		is_bulky_return: Mock,
		is_heavy_return: Mock,
		expected: str,
	):

		is_bulky.return_value = is_bulky_return
		is_heavy.return_value = is_heavy_return

		technical_screen = PackageSorter()
		actual = technical_screen.sort(Mock(), Mock(), Mock(), Mock())

		assert actual == expected

	@pytest.mark.parametrize(
		"width, height, length, expected",
		[
			(150, 1, 1, True),
			(1, 150, 1, True),
			(1, 1, 150, True),
			(1, 1, 1, False),
			(149, 149, 149, True),
			(10, 10, 10, False)
		]
	)
	def test_isBulky(
		self,
		width: int,
		height: int,
		length: int,
		expected: bool
	):
		assert PackageSorter()._isBulky(width, height, length) == expected

	@pytest.mark.parametrize(
		"mass, expected",
		[
			(20, True),
			(19, False),
			(21, True),
			(10, False),
			(0, False)
		]
	)
	def test_isHeavy(
		self, 
		mass: int, 
		expected: bool
	):
		assert PackageSorter()._isHeavy(mass) == expected

