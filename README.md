# Fernando

The Driver

## Message Spec

Format: \<channel> "message"

### Inputs

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
* \<fernando> "?"
  * Queries the current drive condition

### Outputs

* \<fernando.status> "f"
  * The motors have been set to forwards
  * Fired on a state change or in response to a status query
* \<fernando.status> "b"
  * The motors have been set to reverse (backwards)
  * Fired on a state change or in response to a status query
* \<fernando.status> "l"
  * The motors have been set to left rotation on the spot
  * Fired on a state change or in response to a status query
* \<fernando.status> "r"
  * The motors have been set to right rotation on the spot
  * Fired on a state change or in response to a status query
* \<fernando.status> "s"
  * The motors have been set to stop
  * Fired on a state change or in response to a status query