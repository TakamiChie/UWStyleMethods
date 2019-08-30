Remove-Item "uwstyle.egg-info" -Recurse
Remove-Item "dist" -Recurse
Remove-Item "build" -Recurse
python setup.py sdist
python setup.py bdist_wheel
$title = "PyPI upload?"
$message = "The package was created in the `dist` folder. Can I continue uploading to PyPI?"
$tChoiceDescription = "System.Management.Automation.Host.ChoiceDescription"
$options = @(
    New-Object $tChoiceDescription ("Yes(&Y)", "Upload the library to PyPI.")
    New-Object $tChoiceDescription ("No(&N)", "Cancel the upload. The library remains in the `dist` folder.")
)
$result = $host.ui.PromptForChoice($title, $message, $options, 0)
switch ($result)
{
    0 {
      twine upload dist/*
      break
    }
    1 {
      "Cancel the upload. The library remains in the `dist` folder."
      break
    }
}
