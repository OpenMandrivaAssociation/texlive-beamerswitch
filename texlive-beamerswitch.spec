%global tl_name beamerswitch
%global tl_revision 64182

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.9
Release:	%{tl_revision}.1
Summary:	Convenient mode selection in Beamer documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/beamer-contrib/beamerswitch
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamerswitch.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamerswitch.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamerswitch.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This class is a wrapper around the beamer class to make it easier to use
the same document to generate the different forms of the presentation:
the slides themselves, an abbreviated slide set for transparencies or
online reference, an n-up handout version (various layouts are
provided), and a transcript or set of notes using the article class. The
class provides a variety of handout layouts, and allows the mode to be
chosen from the command line (without changing the document itself).

