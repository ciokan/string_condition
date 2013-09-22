import unittest

from base import validate, StringConditionsException


class TestSequenceFunctions(unittest.TestCase):

	def test_simple( self ):
		try:
			validate( "foo bar", ["foo", "bar"] )
		except StringConditionsException:
			self.fail( "Condition failed: foo bar" )

		self.assertRaises( StringConditionsException, validate, "foo bar", ["foo"] )

	def test_and( self ):
		try:
			validate( "foo&bar", ["foo", "bar"] )
		except StringConditionsException:
			self.fail( "Condition failed: foo&bar" )

		self.assertRaises( StringConditionsException, validate, "foo&bar", ["foo"] )

	def test_or( self ):
		try:
			validate( "foo|bar", ["foo"] )
			validate( "foo|bar", ["bar"] )
			validate( "foo|bar", ["foo", "bar"] )
		except StringConditionsException:
			self.fail( "Condition failed: foo|bar" )

		self.assertRaises( StringConditionsException, validate, "foo&bar", [] )

	def test_mixed( self ):
		try:
			validate( "foo&bar|eggs apples", ["foo", "bar", "apples"] )
			validate( "foo&bar|eggs apples", ["foo", "eggs", "apples"] )
			validate( "foo&bar|eggs apples", ["foo", "bar", "eggs", "apples"] )
		except StringConditionsException:
			self.fail( "Condition failed: foo&bar|eggs apples" )

		self.assertRaises( StringConditionsException, validate, "foo&bar|eggs apples", ["foo", "bar"] )


if __name__ == '__main__':
	unittest.main()
