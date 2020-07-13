# Reading Documentation
How do you think developers remember all the different classes and functions they use, all the parameters those functions take, and what values they return? Are they super-brains, who can remember or guess everything they need to know? Maybe some of them are, but the rest of us read documentation. And most experienced developers will tell you that as you get more practiced, the amount of time you spend reading documentation actually _increases_, rather than decreases.

"Documentation" is the name for the text that explains how to use someone else's code. Every class and function in Python has documentation, and every reputable library you can install with `pip` will have documentation as well. Learning to find, interpret, and read that documentation is one of the most important steps to becoming a confident developer. Despite this, there's very little advice about how to get good at this. A lot of documentation is created by automated tools, or written by developers who would rather be doing something else, so it's not always the easiest to understand. But most documentation follows a very consistent format, and once you understand that format it becomes much easier to follow.

Here are three examples of different kinds of documentation, from different libraries. Read these examples alongside the documentation they refer to, and then have a look at the exercises for each section.

## Example One: A Class Method
In this case, we're going to use the documentation for Pandas' `DataFrame.merge` method. `DataFrame.merge` is a complicated method, and I end up looking at the docs nearly every time I use it, just to remind myself exactly how it works.

You can find the documentation for this function [here](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html).

Let's look at it line-by-line, starting with the title of the page.

> `pandas.DataFrame.merge`

The heading of the page says "pandas.DataFrame.merge". That's like a map telling you how to find this method - it's in the `pandas` library, it is a class method of `DataFrame` objects, and it's called `merge`. What "class method" means here is that it's a method that belongs to every "instance" of the `DataFrame` class. If you make a `DataFrame` called `df`, then you'll be able to use the `merge` method by calling `df.merge()`. Incidentally, you can tell that `DataFrame` is a class and not, say, a module within the Pandas library, because its name starts with capital letters - that's a convention in Python that is almost universally adhered to.

> `DataFrame.merge(self, right, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False, sort=False, suffixes=('_x', '_y'), copy=True, indicator=False, validate=None) → 'DataFrame'`

This line is what is sometimes called the "signature" of the method - It tells you method's parameters to which you must pass arguments, and the optional (or "keyword") parameters you can also pass arguments, and the default arguments for those optional parameters. It also tells you what kind of object the method will return. It uses a kind of shorthand notation for this, that closely resembles how you'd write the code if you were using this method.

**TOP HINT:** "Parameter" is the name for something the method expects you to pass it. "Argument" is the name for the specific values or objects that you pass to a method's parameters. 

Right after `DataFrame.merge`, we see `(self, right,`. This tells you that there are two parameters that _must_ be given arguments. The first, `self`, is kind of a special case. Every class method automatically receives a reference to itself as its first argument when it is called, so you don't have to worry about it - for example, if you call `df.merge()`, the `self` parameter will receive a reference to `df`. The second parameter, `right`, you _do_ have to worry about. Calling `merge` will fail unless it receives some value as an argument for `right`. You'd do that by putting the argument into the brackets after you call the `merge` method, like `df.merge(argument_for_right_parameter_goes_here)`. At the moment, we don't know exactly what sort of object it expects to get as an argument for `right`, but we'll find out later.

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

To use this, you'd write something like 

```python
df.merge(another_df, on='common_id') # merging on one column

df.merge(another_df, on=['year', 'zip_code']) # merging on two columns
``` 

Often when you're using a method for the first time (or the hundredth time), it's hard to figure out exactly what the parameter expects as a value. The best way to figure this out is to either experiment with the method, or (better) check out the examples which are often provided at the end of the documentation.

The documentation continues with definitions for each of the method's parameters.

>> **`Returns: DataFrame`**
>>
>> `A DataFrame of the two merged objects.`

Finally, the documentation tells you (again) what the method returns. This time it gives you a little bit more information - that the `DataFrame` returned is the result of merging two `DataFrame` objects (in this case `self` and whatever you passed to the `right` parameter).

>> **`Examples`**

I won't copy in all the text of the examples (getting the formatting right is a pain), but often this section is the most useful part of the documentation. Many times, something that didn't make sense in the documentation above becomes clear when you see an example of how it is used in practice.

### Excercises

* For the `DataFrame.merge` method, what is the default value of the `copy` parameter?
* Look at the documentation for the `DataFrame.drop_duplicates` class method, [here](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop_duplicates.html). What arguments can be passed to the `keep` parameter of this method?
*  **HARD MODE:** In the signature for `DataFrame.drop_duplicates`, the `subset` parameter takes an argument of type `Union[Hashable, Sequence[Hashable], NoneType]`. What the heck does that mean? (hint: look at the more detailed discussion of the parameters later in the documentation)

## Example Two: A Class

Let's look at a different kind of documentation, from a different library. [This](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html) is the documentation for the `sklearn` library's `LinearRegression` class. It's a class that represents a linear regression model. Don't worry if you don't understand much about linear regression, just focus on understanding how to read the documentation. Let's start with the page heading.

> `sklearn.linear_model.LinearRegression`

As with the class method we looked at above, the page title here tells you some useful information. The `LinearRegression` class is found in the `linear_model` module of the `sklearn` library. If you wanted to use an instance of this class in your own code, you'd need to first import it, by running something like 

```python
from sklearn.linear_model import LinearRegression
```

The next line of the documentation is as follows:

> `class sklearn.linear_model.LinearRegression(*, fit_intercept=True, normalize=False, copy_X=True, n_jobs=None)`

Here's the "signature" for the `__init__` method of this class. In other words, it tells you how to make an instance of this class. This section gives you a summary of all of the parameters you can set when you create an instance of the `LinearRegression` class. In other words, it tells you what options you can choose for the kind of linear regression model you want to make.

We can see that there are four "keyword" parameters, i.e. parameters that have default arguments, which we don't need to set. These are `fit_intercept`, `normalize`, `copy_x` and `n_jobs`. Also, check out that cheeky little `*` in there. That's a bit abstruse, so don't pay it much mind. It means that you _can_ pass any number of other arguments, but they will be ignored.

>`Ordinary least squares Linear Regression.`
>
>`LinearRegression fits a linear model with coefficients w = (w1, …, wp) to minimize the residual sum of squares between the observed targets in the dataset, and the targets predicted by the linear approximation.`

This is typical documentation-speak. It describes _exactly_ what the class does, and nothing else. It uses the most precise and technical language possible to define the class's behaviour. This can be extremely frustrating when you're just trying to get a general sense of what something does, but you'll come to appreciate the specificity in many cases. 

> `Parameters:`
>
>> **`fit_intercept: bool, default=True`**
>>
>> `Whether to calculate the intercept for this model. If set to False, no intercept will be used in calculations (i.e. data is expected to be centered).`

Now we get more detail on each of the parameters. In this case it tells you that the `fit_intercept` parameter expects a `bool` (i.e. true or false) argument, and that the default value is `True`. Then it tells you how setting that parameter will affect the behaviour of the `LinearRegression` instance that you create.

There's a description of each of the other parameters here too, but let's skip ahead now to look at the next section of the page.

> `Attributes:`
>
>> **`coef_: array of shape (n_features, ) or (n_targets, n_features)`**
>>
>> `Estimated coefficients for the linear regression problem. If multiple targets are passed during the fit (y 2D), this is a 2D array of shape (n_targets, n_features), while if only one target is passed, this is a 1D array of length n_features.`

"Attributes" describes the attributes you can expect to find in any instance of this class. It tells us the name of the attribute, and the type of data that is stored under that name. So in this case, if we had a an instance of `LinearRegression` called `model`, we'd expect to be able to see the coefficients for that model with `model.coef_`, and that what we would see see there would be of `array` type. Note that this is not a class method! We don't call `model.coef_()`. Why does `coef_` have that trailing underscore? It's a convention of the `sklearn` library, that any attributes which are estimated from data are given a trailing underscore.

There's a few more attributes, and then some "Notes", and then the extremely useful "Examples" section. This example is pretty minimal, but it's great for giving you an accessible overview of how to use the class. "Examples" is often the first section I look at. 

Finally, we get to a section called "Methods".

> **`Methods`**
>> `fit(self, X, y[, sample_weight])    Fit linear model.`
>>
>> `get_params(self[, deep])            Get parameters for this estimator.`
>>
>> `predict(self, X)                    Predict using the linear model.`
>>
>> `score(self, X, y[, sample_weight])  Return the coefficient of determination R^2 of the prediction.`
>>
>> `set_params(self, **params)          Set the parameters of this estimator.`

Here are the "signatures" for all the class methods for the `LinearRegression` class. You'll recognise the format from the class method we looked at in the previous section of this tutorial. What this is telling you is that any instance of `LinearRegression` has five methods you can call for it: `fit`, `get_params`, `predict`, `score`, and `set_params`. Below this section of the documentation, each of these is discussed in greater detail, including information about what is returned by each of these functions. Here, you just get a brief introduction to each of these methods. This is given in the typical terse style. `fit(self, X, y[, sample_weight])` means "the `fit` method has four parameters, `self` (passed automatically to every class method), `X`, `y`, and an optional (i.e. keyword) parameter, `sample_weight`. Here, square brackets are used to denote optional parameters. In `set_params(self, **params)`, the two asterisks (`**`) indicate that this method takes any number of keyword arguments, which will be "unpacked" by the method. You can read more about Python's "unpacking" in [this quite good blog post](https://treyhunner.com/2018/10/asterisks-in-python-what-they-are-and-how-to-use-them/).

After this, we get an in-depth look at each of the class methods. The syntax here is very similar to the documentation of a class method we looked at in the previous section of this tutorial, so I think you will be able to make sense of it.

### Exercises
* What are the names of the parameters of the `LinearRegression.fit` method?
* What is the data type of the `rank_` attribute?
* **HARD MODE:** How many "keyword" parameters does the `__init__` method of the class [`sklearn.feature_extraction.text.CountVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html) take?

## Example Three: A Function

[Here](https://docs.python.org/3/library/functions.html#print) is the documentation for a function you've probably used a hundred times, the `print` function. It's called a "function", rather than a "method", because it doesn't belong to a class. You don't have to create an instance of a class in order to use `print`, you can just go ahead and `print` things.

By now, the format of the "signature" should be pretty familiar to you:

`print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)`

We see that it takes any number of positional arguments which are "unpacked" as `objects` (using the `*` syntax I mentioned above), and then four "keyword" parameters, `sep`, `end`, `file`, and `flush`. Unlike some of the other documentation we've seen, the documentation here is extremely brief. After the signature, we just get a few paragraphs describing what each of the parameters does. As is typical with documentation, this tells you exactly what everything does, but doesn't give you a lot of guidance about how to use them. For example, it's hard to know the right format for using `print` to write to a file. The instruction `The file argument must be an object with a write(string) method` is not very meaningful, even if it is strictly accurate.

### Excercises
* What is the default argument for the `sep` parameter?
* What would you expect to happen if you ran `print("one", "two", "three", sep=" and ")`?
* What kind of argument should you pass to the `ndigits` parameter of the `round` function?

## Conclusions
The practice of writing code mostly involves _reading_. Reading your own code, reading other people's code, and reading documentation. While there's no substitute for experimentation and learning by doing, documentation is an essential tool for understanding how to use the libraries we work with. Don't be discouraged by the terse style of much of the documentation you read - you will come to appreciate its precision and economy. My final piece of advice would be to go and browse the documentation for some functions or classes that you already know well - you may be surprised by what additional things are possible that you never knew about.