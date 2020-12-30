rule Text2Example
{
    strings:
        $text_string = "barfoo"

    condition:
        $text_string
}