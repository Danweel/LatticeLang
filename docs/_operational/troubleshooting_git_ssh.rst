.. _troubleshooting_git_ssh:

Git SSH Authentication Issues
==============================

Symptom
-------
``git push`` prompts for GitHub username and password, even after
authenticating with ``gh auth login -p ssh``.

Cause
-----
The Git remote URL is set to HTTPS (``https://github.com/...``), but
authentication was configured for SSH. The two protocols use different
credential mechanisms — SSH keys are not consulted when connecting
over HTTPS.

Resolution
----------
Switch the remote URL from HTTPS to SSH:

.. code-block:: bash

   git remote set-url origin git@github.com:Danweel/LatticeLang.git

Verify:

.. code-block:: bash

   git remote -v
   # Should show: git@github.com:Danweel/LatticeLang.git

Then push normally:

.. code-block:: bash

   git push origin main

Prevention
----------
When cloning a new repository, use the SSH URL instead of HTTPS:

.. code-block:: bash

   git clone git@github.com:Danweel/LatticeLang.git

If you already cloned via HTTPS, fix it with the ``set-url`` command
above. Running ``gh auth login -p ssh`` configures GitHub CLI
authentication but does **not** change existing Git remote URLs.

Verification Checklist
----------------------
#. ``git remote -v`` shows ``git@github.com:`` (not ``https://github.com/``)
#. ``ssh -T git@github.com`` returns "Hi Danweel! You've successfully authenticated"
#. ``git push`` completes without prompting for credentials