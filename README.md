# openSUSE migration

Provides zypper services with repo definitions as well as `leap-cli` utility to switch between versions (as an alternative to [`tumbleweed-cli`][2]).

### Usage

1. `zypper in opensuse-migration` -- the package will provide a local zypper service;
2. Use zypper as usual until the time for migration comes; 
3. `leap-cli migrate` to choose a migration target;
4. `zypper dup` to upgrade all the packages.

### Installation

Get the RPM package from OBS: [home:ikapelyukhin/opensuse-migration](https://build.opensuse.org/package/show/home:ikapelyukhin/opensuse-migration)

### Demo

See it in action:

[![asciicast](https://asciinema.org/a/iaHZRzqlgQXtcPloHUZcPHZma.svg)](https://asciinema.org/a/iaHZRzqlgQXtcPloHUZcPHZma)

### Gory technical details

#### Zypper service types

1. RIS: XML format, URL is mandatory in service `ini`; `file:` or `dir:` URLs have to point to a directory that contains `repo/repoindex.xml` in it. 
2. Plugin: a script that prints `ini` to STDOUT; repos that come from it are volatile -- can't disable individual repos with `zypper mr -d` (reset on next service refresh).

Additional details can be found in the [documentation][1].

#### Zypper RIS service INI example

```
[service_alias]
name=Service Name
enabled=1
autorefresh=1
url = https://example.org/
type = ris
```
#### Zypper RIS service XML example

```xml
<repoindex ttl="86400">
<repo url="https://example.org/product" alias="Example-Pool" name="Example-Pool" autorefresh="false" enabled="true"/>
<repo url="https://example.org/update" alias="Example-Updates" name="Example-Updates" autorefresh="true" enabled="true"/>
</repoindex>
```

 [1]: https://doc.opensuse.org/projects/libzypp/12.2/zypp-services.html
 [2]: https://github.com/boombatower/tumbleweed-cli