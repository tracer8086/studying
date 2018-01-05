using System;
using System.Collections;
using System.Collections.Generic;

namespace AlgorithmTools
{
    public class Range : IEnumerable<int>
    {
        // Fields of range: [from; to).
        private int from;
        private int to;
        private int delta;

        // Range limits are incapsulated in properties to prevent situation when From > To or To < From.
        public int From
        {
            get => from;

            set
            {
                if (value > to)
                    throw new ArgumentException("Initial position for counting can not be bigger than final position.");

                from = value;
            }
        }

        public int To
        {
            get => to;

            set
            {
                if (value < from)
                    throw new ArgumentException("Final position for counting can not be less than initial position.");

                to = value;
            }
        }

        // Delta is the counting offset. It denotes difference between two nearby elements.
        public int Delta
        {
            get => delta;

            set
            {
                if (value == 0)
                    throw new ArgumentException("Delta must be non-zero.");

                if (value > To - From - 1)
                    throw new ArgumentException("Delta must be less tham difference between From and To.");

                delta = value;
            }
        }

        // Current value of counter; it is set to from value before counting.
        public int Current { get; set; }

        // For situations when it's necessary to get some element of counter by its index.
        public int this[int index]
        {
            get
            {
                int maxIndex = Math.Abs(To - From - 1) / Math.Abs(Delta);

                if (index > maxIndex)
                    throw new IndexOutOfRangeException($"The biggest value of index is {maxIndex}.");

                if (index < 0)
                    throw new IndexOutOfRangeException($"Index must be non-negative.");

                return From + index * Delta;
            }
        }
        
        public Range(int to)
        {
            To = to;
            Current = From = 0;
            Delta = 1;
        }

        public Range(int from, int to, int delta = 1)
        {
            To = to;
            Current = From = from;
            Delta = delta;
        }

        // Counting.
        public IEnumerator<int> GetEnumerator()
        {
            for (Current = from; Current < to; Current += Delta)
                yield return Current;
        }

        IEnumerator IEnumerable.GetEnumerator()
        {
            return GetEnumerator();
        }
    }
}
