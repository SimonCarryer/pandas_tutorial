# Reading Documentation
How do you think developers remember all the different classes and functions they use, all the parameters those functions take, and what values they return? Are they super-brains, who can remember or guess everything they need to know? Maybe some of them are, but the rest of us read documentation. And most experienced developers will tell you that as you get more practiced, the amount of time you spend reading documentation actually _increases_, rather than decreases.

"Documentation" is the name for the text that explains how to use someone else's code. Every class and function in Python has documentation, and every reputable library you can install with `pip` will have documentation as well. Learning to find, interpret, and read that documentation is one of the most important steps to becoming a confident developer. Despite this, there's very little advice about how to get good at this. A lot of documentation is created by automated tools, or written by developers who would rather be doing something else, so it's not always the easiest to understand. But most documentation follows a very consistent format, and once you understand that format it becomes much easier to follow.

## Examples
I think the best way to start learning about documentation is with a few examples

### Example One: A Class Method
In this case, we're going to use the documentation for Pandas' `DataFrame.merge` method. `DataFrame.merge` is a complicated method, and I end up looking at the docs nearly every time I use it, just to remind myself exactly how it works.

You can find the documentation for this function [here](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html).

Let's look at it line-by-line, starting with the title of the page.

> `pandas.DataFrame.merge`

The heading of the page says "pandas.DataFrame.merge". That's like a map telling you how to find this method - it's in the `pandas` library, it is a class method of `DataFrame` objects, and it's called `merge`. What "class method" means here is that it's a method that belongs to every "instance" of the `DataFrame` class. If you make a `DataFrame` called `df`, then you'll be able to use the `merge` method by calling `df.merge()`. Incidentally, you can tell that `DataFrame` is a class and not, say, a module within the Pandas library, because its name starts with capital letters - that's a convention in Python that is almost universally adhered to.

> `DataFrame.merge(self, right, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False, sort=False, suffixes=('_x', '_y'), copy=True, indicator=False, validate=None) → 'DataFrame'`

**TOP HINT:** "Parameter" is the name for something the method expects you to pass it. "Argument" is the name for the specific values or objecst that you pass to a method's parameters. 

This section of the page tells you method's parameters to which you must pass arguments. It also shows the optional (or "keyword") parameters you can also pass arguments, and the default arguments for those optional parameters. It also tells you what kind of object the method will return. It uses a kind of shorthand notation for this, that closely resembles how you'd write the code if you were using this method.

Right after `DataFrame.merge`, we see `(self, right,`. This tells you that there are two parameters that _must_ be given arguments. The first, `self`, is kind of a special case. Every class method automatically receives a reference to itself as its first argument when it is called, so you don't have to worry about it - for example, if you call `df.merge()`, the `self` parameter will receive a reference to `df`. The second parameter, `right`, you _do_ have to worry about. Calling `merge` will fail unless it recieves some value as an argument for `right`. You'd do that by putting the argument into the brackets after you call the `merge` method, like `df.merge(argument_for_right_parameter_goes_here)`. At the moment, we don't know exactly what sort of object it expects to get as an argument for `right`, but we'll find out later.

Now we get to `how='inner'`. This is what's called a "keyword" parameter - we can tell by the `=` after it. It's a parameter that has an argument passed to it by default, in this case it is passed a string, `'inner'`. If we don't tell it any different, it will use `'inner'` as the argument for the `how` parameter. If we wanted to change that, we'd have to explicitly pass it a different value, like this:  `df.merge(argument_for_right_parameter_goes_here, how='some string')`. Because the default argument for `how` is a `string` object, we can assume that `how` expects us to pass it a string, but we don't know exactly what it does with those strings yet, or what strings it will accept.

There's a big list of other keyword parameters after this, which all behave exactly the same way. You can see that many of them, like `left_index` and `right_index`, take a `bool` argument (i.e. `True` or `False`), `suffixes` gets a `tuple` as its default `('_x', '_y')`, and others take `None` as a default, which makes it hard to tell what kind of argument they expect. Nothing here tells you what these parameters actually _do_. That comes later.

There's one last bit, right at the end `) → 'DataFrame'`. This tells you that the method will return a `DataFrame` object. That means that if you ran something like `new_object = df.merge(right_argument)`, then, provided there was no error, `new_object` would refer to a new `DataFrame` that was returned by the `merge` method.

> `Merge DataFrame or named Series objects with a database-style join.`
> 
> `The join is done on columns or indexes. If joining columns on columns, the DataFrame indexes will be ignored. Otherwise if joining indexes on indexes or indexes on a column or columns, the index will be passed on.`

This is the easiest part of the documentation to interpret (usually). It's a plain-text description of what the method does. There's some interesting bits of information in there - the fact that you can join a `DataFrame` or a "named" `Series`, and that you can specify exactly what columns you're joining on.

> `Parameters:`
>
>> **`right: DataFrame or named Series`**
>>
>> `Object to merge with.`

Now we're getting some tasty juice! This is the start of a list that goes into more details about each of the parameters the method accepts. You'll see that it skips over the `self` parameter we saw in the shorthand section above - as discussed, this is automatically passed to class methods, so you don't need to worry about it. It gets straight to the first parameter you _must_ pass to the method, which is called `right`. After the colon it tells you what kinds of objects you can pass to the parameter - a `DataFrame` or a "named" `Series`. I won't get into what a named `Series` is right now. What this means is that when you're using `merge`, you'll probably call it with something like `df.merge(another_df)`.

Now it says `Object to merge with`. That's telling you what the method is going to _do_ with the argument you pass to the `right` parameter. In this case, since we know that the method "Merges DataFrame objects with a database-style join", we can guess that this DataFrame is going to get joined to the DataFrame we're calling `merge` from. I suspect they're calling it `right` here in reference to the "left join/right join" parlance for describing joins in SQL. 

>> **`how: {‘left’, ‘right’, ‘outer’, ‘inner’}, default ‘inner’`**
>> 
>> `Type of merge to be performed.`
>> 
>> * `left: use only keys from left frame, similar to a SQL left  outer join; preserve key order.`
>> 
>> * `right: use only keys from right frame, similar to a SQL right outer join; preserve key order.`
>> 
>> * `outer: use union of keys from both frames, similar to a SQL full outer join; sort keys lexicographically.`
>> 
>> * `inner: use intersection of keys from both frames, similar to a SQL inner join; preserve the order of the left keys.`

This is nice! `how` is a keyword parameter which takes a `string` as an argument. What you see here is a list of all the strings it knows about, and then a description of the different behaviour you get depending on which one you pass it. It also tells you the default value, with is the string `'inner'`. If you pass a `string` to `how` that is not on this list, the method will return an error.

To use this, you'd write something like `df.merge(another_df, how='left')`.

>> **`on: label or list`**
>>
>> `Column or index level names to join on. These must be found in both DataFrames. If on is None and not merging on indexes then this defaults to the intersection of the columns in both DataFrames.`

This is a bit trickier to interpret. Documentation often uses very precise and terse language, and usually assumes that you know the definition of every technical term they use. We can see that `on` expects either a `label` or a `list` for the argument you pass it. It goes on to explain that in this case, this means either a column name that exists in both `DataFrame`s, or else a list of such column names (it will also accept a "named index level", which is too complex to go into right now).

To use this, you'd write something like `df.merge(another_df, on='common_id')`, or else `df.merge(another_df, on=['year', 'zip_code'])` if you're joining on two columns.

Often when you're using a method for the first time (or the hundredth time), it's hard to figure out exactly what the parameter expects as a value. The best way to figure this out is to either experiment with the method, or (better) check out the examples which are often provided at the end of the documentation.

The documentation continues with definitions for each of the method's parameters.

>> **`Returns: DataFrame`**
>>
>> `A DataFrame of the two merged objects.`

Finally, the documentation tells you (again) what the method returns. This time it gives you a little bit more information - that the `DataFrame` returned is the result of merging two `DataFrame` objects (in this case `self` and whatever you passed to the `right` parameter).

>> **`Examples`**

I won't copy in all the text of the examples (getting the formatting right is a pain), but often this section is the most useful part of the documentation. Many times, something that didn't make sense in the documentation above becomes clear when you see an example of how it is used in practice.

### Example Two: A Class

Let's look 

## General Advice

Here are a few tips for working with documentation.

* Note which version of a library you're using. Usually a docs page will default to the latest version of a library, and you might be using an older version. Usually libraries will either have links to documentation for older versions, or else note when a parameter has changed from previous versions. You can check what version of a library you are using from within Python, with something like `pd.__version__`.
* Sometimes it's hard to find the documentation for a specific method or class 