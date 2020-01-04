# Fernando

The Driver

## Prerequisites

- `sudo apt-get install python-systemd`
- `pip install redis`

## Message Spec

Format: \<channel> "message"

**Inputs**

* \<fernando> "f"
  * Set motors to forwards
* \<fernando> "b"
  * Set motors to reverse (backwards)
* \<fernando> "l"
  * Set motors to left rotation on the spot
* \<fernando> "r"
  * Set motors to right rotation on the spot
* \<fernando> "s"
  * Set motors to all stop

**Outputs**

None