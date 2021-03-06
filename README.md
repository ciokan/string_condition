Simple string conditions
================

A small python package which evaluates string based conditions.

As an example let's say you have a class which creates a HTML link
but this link can have some widgets attached to it such as a tooltip,
popover, dropdown, modal etc.

Normally you would declare what widgets are supported by your class in
an array or dict and loop through it to perform the validations
but here comes the tricky part, some widgets don't get
well together. Like the tooltip with the popover or the modal with the
dropdown so you must somehow enforce a condition for each one in part
which takes a lot of time, it's not elegant and not isolated (why should
the tooltip care about the popover?).

As a response to such needs I've created this small library which takes a
string such as `(dropdown modal href) (tooltip popover) title` and evaluates
it so that we can ensure an exception is thrown if we supply both a modal
and a dropdown to the same link for example. The library supports more
trickery so here are a few examples and their 'translations' respectively:

`href&text (dropdown modal) (tooltip popover title)` - `href` and `text` are
required attributes, you can also supply a dropdown or modal and you can also
provide a tooltip, popover or title attribute.

`href&text title|tooltip` - `href` and `text` are required, any or both of
title and tooltip must be provided.

`title|text|href` - any or all must be provided

`title&text` - both are required

`(title&text|tooltip popover)` - one of the group can be provided and it's
either `title + text or tooltip` or `popover`

### To wrap things up ######

`&`  (and) binds values and makes them both required  
`|`  (or) any or all of the values separated by pipe can be supplied  
`()` (exclusive) group of exclusive values (only one value from the group can be supplied) .
The group values can also be glued with either `&` or `|` operators and they
will get evaluated accordingly.

... open to suggestions. For more examples you can read the `tests.py` file

P.S. Usage:

	from string_conditions.base import validate, StringConditionsException

	try:
		validate( "title&text", ["title", "foo", "bar"] )
	except StringConditionsException:
		....
