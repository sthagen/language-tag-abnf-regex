# language-type-abnf-regex

Test repository for the ABNF translation of language type codes into a regular expression for CSAF.

Base information from:
```
[BCP47] Phillips, A. and M. Davis, "Matching of Language Tags", BCP 47, RFC 4647, September 2006. 
        Phillips, A., Ed., and M. Davis, Ed., "Tags for Identifying Languages", BCP 47, RFC 5646, September 2009.
        https://www.rfc-editor.org/info/bcp47
```
Direct link: https://www.rfc-editor.org/rfc/bcp/bcp47.txt

## Status

Experimental.

## Transformation

Here is the regex: `^(([A-Za-z]{2,3}(-[A-Za-z]{3}(-[A-Za-z]{3}){0,2})?|[A-Za-z]{4,8})(-[A-Za-z]{4})?(-([A-Za-z]{2}|[0-9]{3}))?(-([A-Za-z0-9]{5,8}|[0-9][A-Za-z0-9]{3}))*(-[A-WY-Za-wy-z0-9](-[A-Za-z0-9]{2,8})+)*(-x(-[A-Za-z0-9]{1,8})+)?|x(-[A-Za-z0-9]{1,8})+|i-default|i-mingo)$`

And the way to it:
```
Language-Tag = langtag | privateuse | grandfathered

langtag = language(-script)?(-region)?(-variant)*(-extension)*(-privateuse)?

language = ([A-Za-z]{2,3}(-[A-Za-z]{3}(-[A-Za-z]{3}){0,2})?|[A-Za-z]{4,8})
script = [A-Za-z]{4}
region = ([A-Za-z]{2}|[0-9]{3})
variant = ([A-Za-z0-9]{5,8}|[0-9][A-Za-z0-9]{3})
extension = [A-WY-Za-wy-z0-9](-[A-Za-z0-9]{2,8})+

privateuse = x(-[A-Za-z0-9]{1,8})+
grandfathered = i-default|i-mingo
```

Source: @tschmidtb51 in https://github.com/oasis-tcs/csaf/issues/71


**Note**: The default branch is default.
