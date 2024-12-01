import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from queue_interface import NumberQueue, StringQueue, BooleanQueue

def test_number_queue():
    queue = NumberQueue()
    queue.enqueue(10)
    queue.enqueue(20)
    assert not queue.is_empty()
    assert queue.peek() == 10
    assert queue.dequeue() == 10
    assert queue.peek() == 20
    assert queue.dequeue() == 20
    assert queue.is_empty()
    with pytest.raises(IndexError):
        queue.dequeue()
    with pytest.raises(IndexError):
        queue.peek()

def test_string_queue():
    queue = StringQueue()
    queue.enqueue("apple")
    queue.enqueue("banana")
    assert not queue.is_empty()
    assert queue.peek() == "apple"
    assert queue.dequeue() == "apple"
    assert queue.peek() == "banana"
    assert queue.dequeue() == "banana"
    assert queue.is_empty()
    with pytest.raises(IndexError):
        queue.dequeue()
    with pytest.raises(IndexError):
        queue.peek()

def test_boolean_queue():
    queue = BooleanQueue()
    queue.enqueue(True)
    queue.enqueue(False)
    assert not queue.is_empty()
    assert queue.peek() is True
    assert queue.dequeue() is True
    assert queue.peek() is False
    assert queue.dequeue() is False
    assert queue.is_empty()
    with pytest.raises(IndexError):
        queue.dequeue()
    with pytest.raises(IndexError):
        queue.peek()

# my command for compiling through python
# python -m pytest test_queues.py