import logging
from kicker.storage.storage import Storage


def storage_worker(queue, config, filename='games.h5'):
    s = Storage(config, filename=filename)

    while True:
        frame, action = queue.get(True)
        if frame is None:
            logging.debug('break')
            break
        s.add_frame(frame)
        s.add_action(action)

        logging.debug("frames %d", len(s.actions))

        if len(s.actions) > 100:
            s.save()
