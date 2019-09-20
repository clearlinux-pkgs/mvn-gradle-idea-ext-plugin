#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-gradle-idea-ext-plugin
Version  : 0.4.2
Release  : 2
URL      : https://github.com/JetBrains/gradle-idea-ext-plugin/archive/v0.4.2.tar.gz
Source0  : https://github.com/JetBrains/gradle-idea-ext-plugin/archive/v0.4.2.tar.gz
Source1  : https://plugins.gradle.org/m2/gradle/plugin/org/jetbrains/gradle/plugin/idea-ext/gradle-idea-ext/0.4.2/gradle-idea-ext-0.4.2.jar
Source2  : https://plugins.gradle.org/m2/gradle/plugin/org/jetbrains/gradle/plugin/idea-ext/gradle-idea-ext/0.4.2/gradle-idea-ext-0.4.2.pom
Source3  : https://plugins.gradle.org/m2/org/jetbrains/gradle/plugin/idea-ext/org.jetbrains.gradle.plugin.idea-ext.gradle.plugin/0.4.2/org.jetbrains.gradle.plugin.idea-ext.gradle.plugin-0.4.2.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-gradle-idea-ext-plugin-data = %{version}-%{release}
Requires: mvn-gradle-idea-ext-plugin-license = %{version}-%{release}
BuildRequires : buildreq-mvn
BuildRequires : gradle

%description
# gradle-idea-ext-plugin
[![JetBrains team project](http://jb.gg/badges/team.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

%package data
Summary: data components for the mvn-gradle-idea-ext-plugin package.
Group: Data

%description data
data components for the mvn-gradle-idea-ext-plugin package.


%package license
Summary: license components for the mvn-gradle-idea-ext-plugin package.
Group: Default

%description license
license components for the mvn-gradle-idea-ext-plugin package.


%prep
%setup -q -n gradle-idea-ext-plugin-0.4.2

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-gradle-idea-ext-plugin
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/mvn-gradle-idea-ext-plugin/LICENSE.txt
mkdir -p %{buildroot}/usr/share/java/.m2/repository/gradle/plugin/org/jetbrains/gradle/plugin/idea-ext/gradle-idea-ext/0.4.2
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/gradle/plugin/org/jetbrains/gradle/plugin/idea-ext/gradle-idea-ext/0.4.2/gradle-idea-ext-0.4.2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/gradle/plugin/org/jetbrains/gradle/plugin/idea-ext/gradle-idea-ext/0.4.2
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/gradle/plugin/org/jetbrains/gradle/plugin/idea-ext/gradle-idea-ext/0.4.2/gradle-idea-ext-0.4.2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/jetbrains/gradle/plugin/idea-ext/org.jetbrains.gradle.plugin.idea-ext.gradle.plugin/0.4.2
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/jetbrains/gradle/plugin/idea-ext/org.jetbrains.gradle.plugin.idea-ext.gradle.plugin/0.4.2/org.jetbrains.gradle.plugin.idea-ext.gradle.plugin-0.4.2.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/gradle/plugin/org/jetbrains/gradle/plugin/idea-ext/gradle-idea-ext/0.4.2/gradle-idea-ext-0.4.2.jar
/usr/share/java/.m2/repository/gradle/plugin/org/jetbrains/gradle/plugin/idea-ext/gradle-idea-ext/0.4.2/gradle-idea-ext-0.4.2.pom
/usr/share/java/.m2/repository/org/jetbrains/gradle/plugin/idea-ext/org.jetbrains.gradle.plugin.idea-ext.gradle.plugin/0.4.2/org.jetbrains.gradle.plugin.idea-ext.gradle.plugin-0.4.2.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-gradle-idea-ext-plugin/LICENSE.txt
