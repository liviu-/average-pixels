# Change log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/) 
and this project adheres to [Semantic Versioning](http://semver.org/) to the extent that a command line tool can do that.

## [1.2.0-dev]

### Added
- Added a `--version` CLI argument 

### Fixed
- Output filename ignores the extension provided by the user to avoid outputs such as "filename.png.jpg" (issue [#11](https://github.com/liviu-/average-pixels/issues/11))

## [1.1.0]

### Added
- Added an `--unweighted` flag to allow users to apply an unweighted (ordinary) arithmetic mean

### Fixed
- Fix typo in `--help` for `--offset`

## [1.0.0] - 2016-08-26

### Added
- Running version can be accessed via importing the package in the namespace and checking its `__version__` attribute.
- Registered and uploaded on PyPI (`$ pip3 install average-pixels`)

### Changed
- The binary changed name from `average_pixels` to `average-pixels`. Dash is more common among binaries, it's easier to type, and it differentiates between directory and binary.

### Fixed
- Output helpful message if directory is a file.

## [0.1.0]

### Changed
- Updated API to allow different modes and shared arguments. For more information, `$ average_pixels --help`, `$ average_pixels download --help`, and `$ average_pixels local --help`.
- In `local` mode, accept only files that end with a predefined extension.

### Fixed
- Fixed some bugs with the `local` mode where output value was missing, or trailing slash was missing from the directory name.
- Output helpful message if:
    - no images found in `local` mode.
    - directory does not exist in `local` mode.


## 0.0.1 - 2016-08-23

Initial stable release

[1.2.0-dev]: https://github.com/liviu-/average-pixels/compare/v1.1.0...HEAD
[1.1.0]: https://github.com/liviu-/average-pixels/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/liviu-/average-pixels/compare/v0.1.0...v1.0.0
[0.1.0]: https://github.com/liviu-/average-pixels/compare/v0.0.1...v0.1.0
